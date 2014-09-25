# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.db.models import Q


class Migration(DataMigration):

    def forwards(self, orm):
        print([orm.airbornespread, orm.directspread, orm.indirectspread])
        for model in [orm.airbornespread, orm.directspread, orm.indirectspread]:
            offenders = model.objects.filter(Q(transport_delay__name__startswith='0') | Q(transport_delay__name__startswith='No'))
            print(offenders)
            for instance in offenders:
                print("Removing ", instance)
                instance.transport_delay = None
                instance.save()
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        print("Nothing can be done.")

    models = {
        'ScenarioCreator.airbornespread': {
            'Meta': {'object_name': 'AirborneSpread'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            '_spread_method_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'other'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'spread_1km_probability': ('ScenarioCreator.custom_fields.PercentField', [], {}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']", 'default': 'None'}),
            'wind_direction_end': ('django.db.models.fields.PositiveIntegerField', [], {'default': '360'}),
            'wind_direction_start': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'ScenarioCreator.controlmasterplan': {
            'Meta': {'object_name': 'ControlMasterPlan'},
            'destruction_capacity': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'destruction_priority_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'reason, time waiting, production type'"}),
            'destruction_program_delay': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruction_reason_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Basic, Trace fwd direct, Trace fwd indirect, Trace back direct, Trace back indirect, Ring'"}),
            'disable_all_controls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Control Master Plan'"}),
            'units_detected_before_triggering_vaccination': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccination_capacity': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'vaccination_priority_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'reason, time waiting, production type'"})
        },
        'ScenarioCreator.controlprotocol': {
            'Meta': {'object_name': 'ControlProtocol'},
            'cost_of_carcass_disposal_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_destruction_appraisal_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_destruction_cleaning_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_euthanasia_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_indemnification_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_vaccination_additional_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_vaccination_baseline_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'cost_of_vaccination_setup_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'days_to_immunity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destroy_direct_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destroy_direct_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destroy_indirect_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destroy_indirect_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruction_is_a_ring_target': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruction_is_a_ring_trigger': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruction_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'default': '5', 'blank': 'True'}),
            'destruction_ring_radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'detection_is_a_zone_trigger': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'detection_probability_for_observed_time_in_clinical': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'detection_probability_report_vs_first_detection': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'direct_trace_is_a_zone_trigger': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direct_trace_period': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'direct_trace_success_rate': ('ScenarioCreator.custom_fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'exam_direct_back_success_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exam_direct_forward_success_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exam_indirect_forward_success_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'examine_direct_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'examine_direct_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'examine_indirect_back_success_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'examine_indirect_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'examine_indirect_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_trace_is_a_zone_trigger': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'indirect_trace_period': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'indirect_trace_success': ('ScenarioCreator.custom_fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_time_between_vaccinations': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'test_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'test_direct_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'test_direct_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'test_indirect_back_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'test_indirect_forward_traces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'test_sensitivity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'test_specificity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trace_direct_back': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trace_direct_forward': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trace_indirect_back': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trace_indirect_forward': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trace_result_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'trigger_vaccination_ring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_cost_accounting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_destruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_detection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_tracing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_vaccination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vaccinate_detected_units': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vaccination_demand_threshold': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccination_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'default': '5', 'blank': 'True'}),
            'vaccination_ring_radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vaccine_immune_period': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"})
        },
        'ScenarioCreator.directspread': {
            'Meta': {'object_name': 'DirectSpread'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            '_spread_method_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'indirect'"}),
            'contact_rate': ('django.db.models.fields.FloatField', [], {}),
            'distance_distribution': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infection_probability': ('ScenarioCreator.custom_fields.PercentField', [], {}),
            'latent_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'movement_control': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subclinical_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'use_fixed_contact_rate': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ScenarioCreator.disease': {
            'Meta': {'object_name': 'Disease'},
            'disease_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_airborne_spread': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'include_contact_spread': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'use_airborne_exponential_decay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_within_unit_prevalence': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ScenarioCreator.diseaseprogression': {
            'Meta': {'object_name': 'DiseaseProgression'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            'disease_clinical_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'disease_immune_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'disease_latent_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'disease_prevalence': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'disease_subclinical_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ScenarioCreator.diseaseprogressionassignment': {
            'Meta': {'object_name': 'DiseaseProgressionAssignment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['ScenarioCreator.ProductionType']"}),
            'progression': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['ScenarioCreator.DiseaseProgression']"})
        },
        'ScenarioCreator.dynamicblob': {
            'Meta': {'object_name': 'DynamicBlob'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_perimeters': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'ScenarioCreator.indirectspread': {
            'Meta': {'object_name': 'IndirectSpread'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            '_spread_method_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'indirect'"}),
            'contact_rate': ('django.db.models.fields.FloatField', [], {}),
            'distance_distribution': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infection_probability': ('ScenarioCreator.custom_fields.PercentField', [], {}),
            'movement_control': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subclinical_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.ProbabilityFunction']", 'default': 'None'}),
            'use_fixed_contact_rate': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ScenarioCreator.outputsettings': {
            'Meta': {'object_name': 'OutputSettings'},
            '_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Scenario']"}),
            'cost_track_destruction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cost_track_vaccination': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cost_track_zone_surveillance': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'days': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1825'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterations': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'save_daily_events': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_daily_exposures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_daily_unit_states': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_iteration_outputs_for_units': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_map_output': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stop_criteria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'disease-end'"})
        },
        'ScenarioCreator.population': {
            'Meta': {'object_name': 'Population'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_file': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'ScenarioCreator.probabilityfunction': {
            'Meta': {'object_name': 'ProbabilityFunction'},
            'a': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alpha': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alpha2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'beta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'd': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equation_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Triangular'"}),
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mode': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'n': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'p': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            's': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'std_dev': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'theta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_axis_units': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Days'"})
        },
        'ScenarioCreator.productiontype': {
            'Meta': {'object_name': 'ProductionType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        },
        'ScenarioCreator.productiontypepairtransmission': {
            'Meta': {'unique_together': "(('source_production_type', 'destination_production_type'),)", 'object_name': 'ProductionTypePairTransmission'},
            'airborne_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'airborne_spread_pair'", 'to': "orm['ScenarioCreator.AirborneSpread']"}),
            'destination_production_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'used_as_destinations'", 'to': "orm['ScenarioCreator.ProductionType']"}),
            'direct_contact_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'direct_spread_pair'", 'to': "orm['ScenarioCreator.DirectSpread']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_contact_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'indirect_spread_pair'", 'to': "orm['ScenarioCreator.IndirectSpread']"}),
            'source_production_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'used_as_sources'", 'to': "orm['ScenarioCreator.ProductionType']"})
        },
        'ScenarioCreator.protocolassignment': {
            'Meta': {'object_name': 'ProtocolAssignment'},
            '_master_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ControlMasterPlan']"}),
            'control_protocol': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['ScenarioCreator.ControlProtocol']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['ScenarioCreator.ProductionType']"})
        },
        'ScenarioCreator.readallcodes': {
            'Meta': {'object_name': 'ReadAllCodes'},
            '_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            '_code_description': ('django.db.models.fields.TextField', [], {}),
            '_code_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ScenarioCreator.readallcodetypes': {
            'Meta': {'object_name': 'ReadAllCodeTypes'},
            '_code_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            '_code_type_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ScenarioCreator.relationalfunction': {
            'Meta': {'object_name': 'RelationalFunction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'x_axis_units': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Days'"}),
            'y_axis_units': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'ScenarioCreator.relationalpoint': {
            'Meta': {'object_name': 'RelationalPoint'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relational_function': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {})
        },
        'ScenarioCreator.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'en'", 'blank': 'True'}),
            'random_seed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'ScenarioCreator.unit': {
            'Meta': {'object_name': 'Unit'},
            '_population': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Population']"}),
            'days_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'days_left_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'initial_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'S'"}),
            'latitude': ('django_extras.db.models.fields.LatitudeField', [], {}),
            'longitude': ('django_extras.db.models.fields.LongitudeField', [], {}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']"}),
            'user_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'ScenarioCreator.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'radius': ('django.db.models.fields.FloatField', [], {})
        },
        'ScenarioCreator.zoneeffectonproductiontype': {
            'Meta': {'object_name': 'ZoneEffectOnProductionType'},
            'cost_of_surveillance_per_animal_day': ('django_extras.db.models.fields.MoneyField', [], {'decimal_places': '4', 'max_digits': '20', 'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Zone']"}),
            'zone_detection_multiplier': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'zone_direct_movement': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"}),
            'zone_indirect_movement': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'+'", 'to': "orm['ScenarioCreator.RelationalFunction']"})
        }
    }

    complete_apps = ['ScenarioCreator']
    symmetrical = True