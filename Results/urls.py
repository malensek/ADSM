"""URLs is entirely procedural based on the contents of models.py.
This has the advantage that urls automatically update as the models change or are renamed."""

import re

__author__ = 'josiahseaman'

from django.conf.urls import patterns, url  # do not delete this
from Results.models import *  # do not delete this


"""Assumes that the only classes in models.py are models.Model.  Because any class will be given a URL,
whether it is a model or not."""
def generate_urls_from_models(input_file, extra_urls=()):
    assert hasattr(extra_urls, '__getitem__')
    lines = open(input_file, 'r').readlines()
    model_strings = extra_urls  # extra_urls is placed first so that they take precedence over auto-urls
    for line in lines:
        if 'class' in line[:5]:
            model_name = re.split('\W+', line)[1]
            model_strings.append("url('^" + model_name + "/$',                      'Results.views.model_list')")
            # model_strings.append("url('^" + model_name + "/(?P<primary_key>\d+)/$', 'Results.views.edit_entry')")

    output = "patterns('', " + ",\n         ".join(model_strings) + ")"
    return eval(output)


urlpatterns = generate_urls_from_models('Results/models.py',
                                        ["url('^Population/$', 'Results.views.population')",
                                         "url('^Workspace/$', 'ScenarioCreator.views.file_dialog')",  # Same as Input side
                                         "url('^Download/(?P<target>.+)/$', 'ScenarioCreator.views.download_file')",  # Same as Input side
                                         "url('^Inputs/$', 'Results.views.back_to_inputs')",
                                         "url('^RunSimulation/$', 'Results.views.run_simulation')",

                                        ])

