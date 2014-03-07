import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import re

from ScenarioCreator.forms import *  # This is absolutely necessary for dynamic form loading


def save_new_instance(initialized_form, request):
    model_instance = initialized_form.save()  # write to database
    model_title = model_instance.__class__.__name__
    if request.is_ajax():
        msg = {'pk': model_instance.pk, 'title': str(model_instance), 'model': model_title, 'status': 'success'}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    return redirect('/setup/%s/%i/' % (model_title, model_instance.pk))  # redirect to edit URL


def new_form(request, initialized_form, context):
    if initialized_form.is_valid():
        return save_new_instance(initialized_form, request)
    return render(request, 'ScenarioCreator/new.html', context)  # render in validation error messages


def get_model_name_and_form(request):
    model_name = re.split('\W+', request.path)[2]  # Second word in the URL
    form = globals()[model_name + 'Form']  # depends on naming convention
    return model_name, form


def initialize_from_existing_model(primary_key, request):
    model_name, form_class = get_model_name_and_form(request)
    model = get_object_or_404(form_class.Meta.model, pk=primary_key)
    initialized_form = form_class(request.POST or None, instance=model)
    return initialized_form, model_name


'''New / Edit / Copy trio that are called from URLs'''
def new_entry(request):
    model_name, form = get_model_name_and_form(request)
    initialized_form = form(request.POST or None)
    context = {'form': initialized_form,
               'title': "Create a new " + model_name}
    return new_form(request, initialized_form, context)


def edit_entry(request, primary_key):
    initialized_form, model_name = initialize_from_existing_model(primary_key, request)
    if initialized_form.is_valid() and request.method == 'POST':
        initialized_form.save()  # write instance updates to database
    context = {'form': initialized_form,
               'title': "Edit a " + model_name}
    return render(request, 'ScenarioCreator/new.html', context)


def copy_entry(request, primary_key):
    initialized_form, model_name = initialize_from_existing_model(primary_key, request)

    if initialized_form.is_valid() and request.method == 'POST':
        initialized_form.instance.pk = None  # This will cause a new instance to be created
        return save_new_instance(initialized_form, request)
    context = {'form': initialized_form,
               'title': "Copy a " + model_name}
    return render(request, 'ScenarioCreator/new.html', context)