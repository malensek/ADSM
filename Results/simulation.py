import os
from collections import defaultdict
import multiprocessing
import time
import platform
import subprocess
from django.db import transaction, close_old_connections
from django.conf import settings


from Results.interactive_graphing import population_zoom_png
from ADSMSettings.views import save_scenario
from ADSMSettings.utils import adsm_executable_command
from ADSMSettings.models import SimulationProcessRecord, SmSession
from Results.models import DailyReport, DailyControls, DailyByZoneAndProductionType, DailyByProductionType, DailyByZone, ResultsVersion
from Results.utils import zip_map_directory_if_it_exists
from ScenarioCreator.models import ProductionType, Zone




def non_empty_lines(line):
    output_lines = []
    line = line.decode("utf-8").strip()
    if len(line):
        output_lines += line.split('\n')  # entries can be more than one line
    return output_lines


def set_pragma(setting, value, connection='default'):
    from django.db import connections

    cursor = connections[connection].cursor()
    raw_sql = "PRAGMA {0} = {1}".format(setting, value)

    cursor.execute(raw_sql)


def simulation_process(iteration_number, adsm_cmd, production_types, zones, testing=False):
    start = time.time()

    if testing:
        for database in settings.DATABASES:
            settings.DATABASES[database]['NAME'] = settings.DATABASES[database]['TEST']['NAME'] if 'TEST' in settings.DATABASES[database] else settings.DATABASES[database]['TEST_NAME']

    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    
    simulation = subprocess.Popen(adsm_cmd,
                                  shell=(platform.system() != 'Darwin'),
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  bufsize=1)
    headers = simulation.stdout.readline().decode()
    from Results.output_parser import DailyParser
    p = DailyParser(headers, production_types, zones)
    adsm_result = []
    prev_line = ''
    while True:
        line = simulation.stdout.readline()  # TODO: Has the potential to lock up if CEngine crashes (blocking io)
        line = line.decode().strip()
        if not line:
            break
        parse_result = p.parse_daily_strings(prev_line, False)
        adsm_result.extend(parse_result)
        prev_line = line
    adsm_result.extend(p.parse_daily_strings(prev_line, last_line=True, create_version_entry=iteration_number==1))

    with transaction.atomic(using='scenario_db'):
        prev_line = ''
        unit_stats_headers = simulation.stdout.readline().decode()  # TODO: Currently we don't use the headers to find which row to insert into.
        for line in simulation.stdout.readlines():
            line = line.decode().strip()
            p.parse_unit_stats_string(prev_line)
            prev_line = line
        p.parse_unit_stats_string(prev_line)

    outs, errors = simulation.communicate()  # close p.stdout, wait for the subprocess to exit
    if errors:  # this will only print out error messages after the simulation has halted
        print(errors)
    
    sorted_results = defaultdict(lambda: [] )
    for result in adsm_result:
        result_type = type(result).__name__
        sorted_results[result_type].append(result)

    set_pragma("synchronous", "OFF", connection='scenario_db')
    set_pragma("journal_mode", "MEMORY", connection='scenario_db')

    DailyReport.objects.bulk_create(sorted_results['DailyReport'])
    DailyControls.objects.bulk_create(sorted_results['DailyControls'])
    DailyByZoneAndProductionType.objects.bulk_create(sorted_results['DailyByZoneAndProductionType'])
    DailyByProductionType.objects.bulk_create(sorted_results['DailyByProductionType'])
    DailyByZone.objects.bulk_create(sorted_results['DailyByZone'])
    try:
        ResultsVersion.objects.bulk_create(sorted_results['ResultsVersion'])
    except KeyError:
        pass

    end = time.time()
    
    # profiler.disable()
    # profiler.dump_stats("parser.prof")
    # stats = pstats.Stats("parser.prof")
    # stats.sort_stats('time')
    # stats.print_stats(10)
    
    return iteration_number, end-start


class Simulation(multiprocessing.Process):
    import django
    django.setup()

    testing = False

    """Execute system commands in a separate thread so as not to interrupt the webpage.
    Saturate the computer's processors with parallel simulation iterations"""
    def __init__(self, max_iteration, testing=False, **kwargs):
        super(Simulation, self).__init__(**kwargs)
        self.max_iteration = max_iteration
        self.production_types = ProductionType.objects.values_list('id', 'name')
        self.zones = Zone.objects.values_list('id', 'name')
        self.testing = testing

    def run(self):
        pid = os.getpid()

        if self.testing:
            for database in settings.DATABASES:
                settings.DATABASES[database]['NAME'] = settings.DATABASES[database]['TEST']['NAME'] if 'TEST' in settings.DATABASES[database] else settings.DATABASES[database]['TEST_NAME']

        simRecord = SimulationProcessRecord(is_parser=False, pid=pid)
        try:
            print("Starting run")

            simRecord.save()

            num_cores = multiprocessing.cpu_count()
            if num_cores > 2:
                num_cores -= 1
            executable_cmd = adsm_executable_command()  # only want to do this once
            statuses = []
            pool = multiprocessing.Pool(num_cores)
            for iteration in range(1, self.max_iteration + 1):
                adsm_cmd = executable_cmd + ['-i', str(iteration)]
                res = pool.apply_async(func=simulation_process, args=(iteration, adsm_cmd, self.production_types, self.zones, self.testing))
                statuses.append(res)

            pool.close()

            simulation_times = []
            for status in statuses:
                iteration_number, s_time = status.get()
                stream = SmSession.objects.get()
                stream.iteration_text += "<li>Iteration %i:  %is </li>" % (iteration_number, s_time)
                stream.save()
                simulation_times.append(round(s_time))

            print(''.join(str(s) + 's, ' for s in simulation_times))
            print("Average Time:", round(sum(simulation_times)/len(simulation_times), 2), 'seconds')
            population_zoom_png()
            zip_map_directory_if_it_exists()
            save_scenario()
            close_old_connections()
        except:
            raise
        finally:
            if simRecord.id:
                simRecord.delete()