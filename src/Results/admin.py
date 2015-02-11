from django.contrib import admin
from django.db.models.loading import get_models, get_app

# Register your models here.
for myModel in get_models(get_app("Results")):
    admin.site.register(myModel)