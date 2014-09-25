from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_hooks()
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ControlMasterPlan.destruction_program_delay'
        db.alter_column('ScenarioCreator_controlmasterplan', 'destruction_program_delay', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlMasterPlan.units_detected_before_triggering_vaccination'
        db.alter_column('ScenarioCreator_controlmasterplan', 'units_detected_before_triggering_vaccination', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccination_priority'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccination_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.minimum_time_between_vaccinations'
        db.alter_column('ScenarioCreator_controlprotocol', 'minimum_time_between_vaccinations', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.direct_trace_period'
        db.alter_column('ScenarioCreator_controlprotocol', 'direct_trace_period', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.destruction_priority'
        db.alter_column('ScenarioCreator_controlprotocol', 'destruction_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.indirect_trace_period'
        db.alter_column('ScenarioCreator_controlprotocol', 'indirect_trace_period', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccination_demand_threshold'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccination_demand_threshold', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccinate_retrospective_days'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccinate_retrospective_days', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ControlProtocol.days_to_immunity'
        db.alter_column('ScenarioCreator_controlprotocol', 'days_to_immunity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Unit._cum_vaccinated'
        db.alter_column('ScenarioCreator_unit', '_cum_vaccinated', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Unit._cum_detected'
        db.alter_column('ScenarioCreator_unit', '_cum_detected', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Unit._cum_infected'
        db.alter_column('ScenarioCreator_unit', '_cum_infected', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Unit.initial_size'
        db.alter_column('ScenarioCreator_unit', 'initial_size', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Unit._cum_destroyed'
        db.alter_column('ScenarioCreator_unit', '_cum_destroyed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'OutputSettings.iterations'
        db.alter_column('ScenarioCreator_outputsettings', 'iterations', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'OutputSettings.days'
        db.alter_column('ScenarioCreator_outputsettings', 'days', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'OutputSettings.maximum_iterations_for_daily_output'
        db.alter_column('ScenarioCreator_outputsettings', 'maximum_iterations_for_daily_output', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ProbabilityFunction.s'
        db.alter_column('ScenarioCreator_probabilityfunction', 's', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ProbabilityFunction.n'
        db.alter_column('ScenarioCreator_probabilityfunction', 'n', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ProbabilityFunction.m'
        db.alter_column('ScenarioCreator_probabilityfunction', 'm', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ProbabilityFunction.d'
        db.alter_column('ScenarioCreator_probabilityfunction', 'd', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'AirborneSpread.wind_direction_end'
        db.alter_column('ScenarioCreator_airbornespread', 'wind_direction_end', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'AirborneSpread.wind_direction_start'
        db.alter_column('ScenarioCreator_airbornespread', 'wind_direction_start', self.gf('django.db.models.fields.PositiveIntegerField')())

    def backwards(self, orm):

        # Changing field 'ControlMasterPlan.destruction_program_delay'
        db.alter_column('ScenarioCreator_controlmasterplan', 'destruction_program_delay', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlMasterPlan.units_detected_before_triggering_vaccination'
        db.alter_column('ScenarioCreator_controlmasterplan', 'units_detected_before_triggering_vaccination', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccination_priority'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccination_priority', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.minimum_time_between_vaccinations'
        db.alter_column('ScenarioCreator_controlprotocol', 'minimum_time_between_vaccinations', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.direct_trace_period'
        db.alter_column('ScenarioCreator_controlprotocol', 'direct_trace_period', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.destruction_priority'
        db.alter_column('ScenarioCreator_controlprotocol', 'destruction_priority', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.indirect_trace_period'
        db.alter_column('ScenarioCreator_controlprotocol', 'indirect_trace_period', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccination_demand_threshold'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccination_demand_threshold', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.vaccinate_retrospective_days'
        db.alter_column('ScenarioCreator_controlprotocol', 'vaccinate_retrospective_days', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ControlProtocol.days_to_immunity'
        db.alter_column('ScenarioCreator_controlprotocol', 'days_to_immunity', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Unit._cum_vaccinated'
        db.alter_column('ScenarioCreator_unit', '_cum_vaccinated', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Unit._cum_detected'
        db.alter_column('ScenarioCreator_unit', '_cum_detected', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Unit._cum_infected'
        db.alter_column('ScenarioCreator_unit', '_cum_infected', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Unit.initial_size'
        db.alter_column('ScenarioCreator_unit', 'initial_size', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Unit._cum_destroyed'
        db.alter_column('ScenarioCreator_unit', '_cum_destroyed', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'OutputSettings.iterations'
        db.alter_column('ScenarioCreator_outputsettings', 'iterations', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'OutputSettings.days'
        db.alter_column('ScenarioCreator_outputsettings', 'days', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'OutputSettings.maximum_iterations_for_daily_output'
        db.alter_column('ScenarioCreator_outputsettings', 'maximum_iterations_for_daily_output', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ProbabilityFunction.s'
        db.alter_column('ScenarioCreator_probabilityfunction', 's', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ProbabilityFunction.n'
        db.alter_column('ScenarioCreator_probabilityfunction', 'n', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ProbabilityFunction.m'
        db.alter_column('ScenarioCreator_probabilityfunction', 'm', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ProbabilityFunction.d'
        db.alter_column('ScenarioCreator_probabilityfunction', 'd', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AirborneSpread.wind_direction_end'
        db.alter_column('ScenarioCreator_airbornespread', 'wind_direction_end', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AirborneSpread.wind_direction_start'
        db.alter_column('ScenarioCreator_airbornespread', 'wind_direction_start', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'ScenarioCreator.airbornespread': {
            'Meta': {'object_name': 'AirborneSpread'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            '_spread_method_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'other'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'spread_1km_probability': ('django_extras.db.models.fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'wind_direction_end': ('django.db.models.fields.PositiveIntegerField', [], {'default': '360'}),
            'wind_direction_start': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'ScenarioCreator.controlmasterplan': {
            'Meta': {'object_name': 'ControlMasterPlan'},
            'destruction_capacity': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'destruction_priority_order': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'destruction_program_delay': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruction_reason_order': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Basic, Trace fwd direct, Trace fwd indirect, Trace back direct, Trace back indirect, Ring'"}),
            'disable_all_controls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'units_detected_before_triggering_vaccination': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccination_capacity': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'vaccination_priority_order': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ScenarioCreator.controlprotocol': {
            'Meta': {'object_name': 'ControlProtocol'},
            'cost_of_carcass_disposal_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_destruction_appraisal_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_destruction_cleaning_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_euthanasia_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_indemnification_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_vaccination_additional_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_vaccination_baseline_per_animal': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'cost_of_vaccination_setup_per_unit': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
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
            'detection_probability_for_observed_time_in_clinical': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'detection_probability_report_vs_first_detection': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'direct_trace_is_a_zone_trigger': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direct_trace_period': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'direct_trace_success_rate': ('django_extras.db.models.fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
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
            'indirect_trace_success': ('django_extras.db.models.fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_time_between_vaccinations': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'test_delay': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
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
            'trace_result_delay': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.ProbabilityFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'trigger_vaccination_ring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_cost_accounting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_destruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_detection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_tracing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_vaccination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vaccinate_detected_units': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vaccinate_retrospective_days': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccination_demand_threshold': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccination_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'default': '5', 'blank': 'True'}),
            'vaccination_ring_radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vaccine_immune_period': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.ProbabilityFunction']", 'blank': 'True', 'related_name': "'+'"})
        },
        'ScenarioCreator.customoutputs': {
            'Meta': {'object_name': 'CustomOutputs', '_ormbases': ['ScenarioCreator.OutputSettings']},
            'all_units_states': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'clock_time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'disease_duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'num_animals_in_each_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'num_animals_in_each_state_by_production_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'num_units_in_each_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'num_units_in_each_state_by_production_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'outbreak_duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'outputsettings_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['ScenarioCreator.OutputSettings']", 'primary_key': 'True'}),
            'tsdA': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"}),
            'tsdU': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'never'"})
        },
        'ScenarioCreator.directspread': {
            'Meta': {'object_name': 'DirectSpread'},
            '_disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Disease']"}),
            '_spread_method_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'indirect'"}),
            'contact_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'distance_distribution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infection_probability': ('django_extras.db.models.fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'latent_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'movement_control': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.RelationalFunction']", 'related_name': "'+'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'subclinical_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
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
            'disease_clinical_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'disease_immune_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'disease_latent_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'disease_prevalence': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'disease_subclinical_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ScenarioCreator.diseaseprogressionassignment': {
            'Meta': {'object_name': 'DiseaseProgressionAssignment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['ScenarioCreator.ProductionType']"}),
            'progression': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.DiseaseProgression']", 'blank': 'True'})
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
            'contact_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'distance_distribution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infection_probability': ('django_extras.db.models.fields.PercentField', [], {'null': 'True', 'blank': 'True'}),
            'movement_control': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.RelationalFunction']", 'related_name': "'+'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'subclinical_animals_can_infect_others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transport_delay': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProbabilityFunction']", 'related_name': "'+'"}),
            'use_fixed_contact_rate': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ScenarioCreator.outputsettings': {
            'Meta': {'object_name': 'OutputSettings'},
            '_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Scenario']"}),
            'cost_track_destruction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cost_track_vaccination': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cost_track_zone_surveillance': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'daily_states_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'days': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterations': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_directory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'maximum_iterations_for_daily_output': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'default': '3', 'blank': 'True'}),
            'save_all_daily_outputs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_daily_events': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_daily_exposures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_iteration_outputs_for_units': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stop_criteria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'disease-end'"}),
            'write_map_output': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'ScenarioCreator.productiontypepairtransmission': {
            'Meta': {'object_name': 'ProductionTypePairTransmission', 'unique_together': "(('source_production_type', 'destination_production_type'),)"},
            'airborne_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.AirborneSpread']", 'blank': 'True', 'related_name': "'airborne_spread_pair'"}),
            'destination_production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']", 'related_name': "'used_as_destinations'"}),
            'direct_contact_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.DirectSpread']", 'blank': 'True', 'related_name': "'direct_spread_pair'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_contact_spread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.IndirectSpread']", 'blank': 'True', 'related_name': "'indirect_spread_pair'"}),
            'source_production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']", 'related_name': "'used_as_sources'"})
        },
        'ScenarioCreator.protocolassignment': {
            'Meta': {'object_name': 'ProtocolAssignment'},
            '_master_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ControlMasterPlan']"}),
            'control_protocol': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.ControlProtocol']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
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
            '_cum_destroyed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_cum_detected': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_cum_infected': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_cum_vaccinated': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_final_control_state_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            '_final_detection_state_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            '_final_state_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            '_population': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Population']"}),
            'days_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'days_left_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'initial_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'S'"}),
            'latitude': ('django_extras.db.models.fields.LatitudeField', [], {}),
            'longitude': ('django_extras.db.models.fields.LongitudeField', [], {}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']"}),
            'user_defined_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_defined_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_defined_3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_defined_4': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'ScenarioCreator.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_description': ('django.db.models.fields.TextField', [], {}),
            'zone_radius': ('django.db.models.fields.FloatField', [], {})
        },
        'ScenarioCreator.zoneeffectonproductiontype': {
            'Meta': {'object_name': 'ZoneEffectOnProductionType'},
            'cost_of_surveillance_per_animal_day': ('django_extras.db.models.fields.MoneyField', [], {'default': '0.0', 'decimal_places': '4', 'max_digits': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.ProductionType']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ScenarioCreator.Zone']"}),
            'zone_detection_multiplier': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'zone_direct_movement': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"}),
            'zone_indirect_movement': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ScenarioCreator.RelationalFunction']", 'blank': 'True', 'related_name': "'+'"})
        }
    }

    complete_apps = ['ScenarioCreator']