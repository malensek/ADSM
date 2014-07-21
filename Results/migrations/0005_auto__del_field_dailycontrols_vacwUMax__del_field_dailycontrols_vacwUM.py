# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DailyControls.vacwUMax'
        db.delete_column('Results_dailycontrols', 'vacwUMax')

        # Deleting field 'DailyControls.vacwUMaxDay'
        db.delete_column('Results_dailycontrols', 'vacwUMaxDay')

        # Deleting field 'DailyControls.vacwAMaxDay'
        db.delete_column('Results_dailycontrols', 'vacwAMaxDay')

        # Deleting field 'DailyControls.vacwAMax'
        db.delete_column('Results_dailycontrols', 'vacwAMax')

        # Deleting field 'DailyControls.vacwUDaysInQueue'
        db.delete_column('Results_dailycontrols', 'vacwUDaysInQueue')

        # Deleting field 'DailyControls.vacwADaysInQueue'
        db.delete_column('Results_dailycontrols', 'vacwADaysInQueue')

        # Deleting field 'DailyControls.vacwUTimeAvg'
        db.delete_column('Results_dailycontrols', 'vacwUTimeAvg')

        # Deleting field 'DailyControls.vacwUTimeMax'
        db.delete_column('Results_dailycontrols', 'vacwUTimeMax')


    def backwards(self, orm):
        # Adding field 'DailyControls.vacwUMax'
        db.add_column('Results_dailycontrols', 'vacwUMax',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwUMaxDay'
        db.add_column('Results_dailycontrols', 'vacwUMaxDay',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwAMaxDay'
        db.add_column('Results_dailycontrols', 'vacwAMaxDay',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwAMax'
        db.add_column('Results_dailycontrols', 'vacwAMax',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwUDaysInQueue'
        db.add_column('Results_dailycontrols', 'vacwUDaysInQueue',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwADaysInQueue'
        db.add_column('Results_dailycontrols', 'vacwADaysInQueue',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwUTimeAvg'
        db.add_column('Results_dailycontrols', 'vacwUTimeAvg',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DailyControls.vacwUTimeMax'
        db.add_column('Results_dailycontrols', 'vacwUTimeMax',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)


    models = {
        'Results.dailybyproductiontype': {
            'Meta': {'object_name': 'DailyByProductionType'},
            'day': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descADet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descADirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descADirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descAIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descAIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descAUnsp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUDet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'descUUnsp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnADet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnADirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnADirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnAIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnAIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnAUnsp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUDet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'desnUUnsp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswA': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswU': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcAClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcATest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcUClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcUTest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnAClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnATest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnUClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detnUTest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcADet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcADirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcADirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcAIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcAIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUDet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcUIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmcURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnADet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnADirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnADirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnAIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnAIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUDet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnUIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'exmnURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcA': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcAAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcU': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcUAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expcUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnA': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnAAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnU': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnUAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'expnUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestruction': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionDet': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionRing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDestructionUnsp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDetection': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDetectionClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDetectionTest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstVaccination': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstVaccinationRing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infcA': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcAAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcU': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcUAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infcUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnA': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnAAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnU': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnUAir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'infnUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'lastDetection': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'lastDetectionClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'lastDetectionTest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['ScenarioCreator.ProductionType']"}),
            'trcAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcAAllp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcADirp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcAIndp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUAllp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUDirp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trcUIndp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnAAllp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnADir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnADirp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnAInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnAIndp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUAllp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUDir': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUDirp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUInd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'trnUIndp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdAClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdADest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdALat': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdANImm': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdASubc': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdASusc': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdAVImm': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUClin': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUDest': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdULat': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUNImm': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUSubc': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUSusc': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tsdUVImm': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcADirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcADirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcAIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcAIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUDirBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUDirFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUFalseNeg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUFalsePos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUIndBack': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUIndFwd': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUTrueNeg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstcUTruePos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstnUFalseNeg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstnUFalsePos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstnUTrueNeg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tstnUTruePos': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnAIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnARing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnUIni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacnURing': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwAAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwADaysInQueue': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwAMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwAMaxDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwATimeAvg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwATimeMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUDaysInQueue': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUMaxDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUTimeAvg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vacwUTimeMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'Results.dailybyzone': {
            'Meta': {'object_name': 'DailyByZone'},
            'day': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'finalZoneArea': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'finalZonePerimeter': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'maxZoneArea': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'maxZoneAreaDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'maxZonePerimeter': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'maxZonePerimeterDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'num_separate_areas': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['ScenarioCreator.Zone']"}),
            'zoneArea': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'zonePerimeter': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'Results.dailybyzoneandproductiontype': {
            'Meta': {'object_name': 'DailyByZoneAndProductionType'},
            'animalDaysInZone': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['ScenarioCreator.ProductionType']"}),
            'unitDaysInZone': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'unitsInZone': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['ScenarioCreator.Zone']"})
        },
        'Results.dailycontrols': {
            'Meta': {'object_name': 'DailyControls'},
            'adqcUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'adqnUAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'average_prevalence': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'costSurveillance': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'costsTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrAppraisal': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrCleaning': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrDisposal': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrEuthanasia': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrIndemnification': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrOccurred': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'destrSubtotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswADaysInQueue': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswAMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswAMaxDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswATimeAvg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswATimeMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswUDaysInQueue': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswUMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswUMaxDay': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswUTimeAvg': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'deswUTimeMax': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detOccurred': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'detcUqAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'diseaseDuration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDetAInfAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'firstDetUInfAll': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'outbreakDuration': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccOccurred': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccSetup': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccSubtotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'vaccVaccination': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'Results.dailyreport': {
            'Meta': {'object_name': 'DailyReport'},
            'full_line': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sparse_dict': ('django.db.models.fields.TextField', [], {})
        },
        'ScenarioCreator.productiontype': {
            'Meta': {'object_name': 'ProductionType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'ScenarioCreator.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'radius': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['Results']