from concurrent.futures import ProcessPoolExecutor
import threading
from django.shortcuts import render, get_object_or_404, redirect
import subprocess
from Results.models import OutputManager, DailyReport
from ScenarioCreator.views import get_model_name_and_model, spaces_for_camel_case, list_per_model


def back_to_inputs(request):
    # Modal confirmation: "Modifying Inputs will delete any Results created and require you to re-run the simulation"
    return redirect('/setup/')


def population(request):
    return redirect('/setup/')


def append_non_empty_lines(line, output_lines):
    line = line.strip()
    if len(line):
        output_lines += line.split('\n')  # the last entry can be more than one line


def read_unicode_line(simulation):
    return simulation.stdout.readline().decode("utf-8")


def simulation_process():
    print("Running")
    simulation = subprocess.Popen(['adsm.exe', 'activeSession.sqlite3'], stdout=subprocess.PIPE)
    output_lines = []
    headers = read_unicode_line(simulation)  # first line should be the column headers
    print(headers)
    while simulation.poll() is None:  # simulation is still running
        line = read_unicode_line(simulation)
        append_non_empty_lines(line, output_lines)  # This blocks until it receives a newline.
        if len(output_lines) > 9:
            DailyReport.objects.bulk_create(headers, output_lines)
            output_lines = []
    # When the subprocess terminates there might be unconsumed output that still needs to be processed.
    append_non_empty_lines(simulation.stdout.read().decode("utf-8"), output_lines)  # notice read() not readline()
    DailyReport.objects.bulk_create(headers, output_lines)
    print("Simulation completed in", len(output_lines), 'days')
    return '%i: Success' % 1


class Simulation(threading.Thread):
    """execute system commands in a separate thread so as not to interrupt the webpage.
    Saturate the computer's processors with parallel simulation iterations"""
    def run(self):
        print(simulation_process())
        # with ProcessPoolExecutor() as executor:
        #     exit_statuses = executor.map(run_iteration, list(range(5)))
        #     print(exit_statuses)


def run_simulation(request):
    context = {'outputs_done': False,}
    sim = Simulation()
    sim.start() # starts a new thread
    return render(request, 'Results/SimulationProgress.html', context)


def list_per_model(model_name, model, iteration=1):
    context = {'entries': model.objects.filter(iteration=iteration)[:200],
               'class': model_name,
               'name': spaces_for_camel_case(model_name)}
    return context


def model_list(request):
    model_name, model = get_model_name_and_model(request, 'Results')
    context = {'title': spaces_for_camel_case(model_name),
               'models': [list_per_model(model_name, model)]}
    return render(request, 'ScenarioCreator/ModelList.html', context)

