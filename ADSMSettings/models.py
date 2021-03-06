from django.db import models

from ADSM import __version__


class SimulationProcessRecord(models.Model):
    is_parser = models.BooleanField(default=True)
    pid = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)


class SingletonManager(models.Manager):
    def get(self, **kwargs):
        if kwargs:
            return self.get_or_create(**kwargs)[0]
        else:
            return super(SingletonManager, self).get_or_create(id=1)[0]

    def get_or_create(self, **kwargs):
        kwargs.pop('id', None)  # make sure there's no id specified
        kwargs.pop('pk', None)
        try:  # modify an existing copy by overwriting with additional values
            result = super(SingletonManager, self).get()
            for key in kwargs:
                setattr(result, key, kwargs[key])
            if len(kwargs):
                result.save()
            return result, False
        except:
            return super(SingletonManager, self).get_or_create(id=1, **kwargs)

    def create(self, **kwargs):
        return self.get_or_create(**kwargs)[0]
    

class SmSession(models.Model):
    scenario_filename = models.CharField(max_length=255, default="Untitled Scenario", blank=True)
    unsaved_changes = models.BooleanField(default=False)
    update_available = models.CharField(max_length=25, default=None, null=True, blank=True, help_text='Is there are new version of ADSM available?')
    simulation_version = models.CharField(max_length=25, default=None, null=True, blank=True, help_text='ADSM Simulation version.')
    population_upload_status = models.CharField(default='', null=True, blank=True, max_length=255)
    population_upload_percent = models.FloatField(default=0)
    simulation_has_started = models.BooleanField(default=False)
    iteration_text = models.TextField(default='')
    show_help_text = models.BooleanField(default=True)
    calculating_summary_csv = models.BooleanField(default=False)


    @property
    def current_version(self):
        return __version__

    def set_population_upload_status(self, status=None, percent=None):
        if status:
            self.population_upload_status = status
        if percent:
            self.population_upload_percent = float(percent)
        self.save()

    def reset_population_upload_status(self):
        self.population_upload_status = None
        self.population_upload_percent = 0
        self.save()
    
    ## Singleton code
    objects = SingletonManager()
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.id=1
        return super(SmSession, self).save(force_insert, force_update, using, update_fields)


def unsaved_changes(new_value=None):
    session = SmSession.objects.get()  # This keeps track of the state for all views and is used by basic_context
    if new_value is not None:  # you can still set it to False
        session.unsaved_changes = new_value
        session.save()
    return session.unsaved_changes


