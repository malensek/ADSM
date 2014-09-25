# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DailyByProductionType.desnUUnsp'
        db.delete_column(u'Results_dailybyproductiontype', 'desnUUnsp')

        # Deleting field 'DailyByProductionType.descUUnsp'
        db.delete_column(u'Results_dailybyproductiontype', 'descUUnsp')

        # Deleting field 'DailyByProductionType.descAUnsp'
        db.delete_column(u'Results_dailybyproductiontype', 'descAUnsp')

        # Deleting field 'DailyByProductionType.firstDestructionIni'
        db.delete_column(u'Results_dailybyproductiontype', 'firstDestructionIni')

        # Deleting field 'DailyByProductionType.desnAUnsp'
        db.delete_column(u'Results_dailybyproductiontype', 'desnAUnsp')

        # Deleting field 'DailyByProductionType.firstDestructionUnsp'
        db.delete_column(u'Results_dailybyproductiontype', 'firstDestructionUnsp')

        # Adding field 'DailyByProductionType.adqcU'
        db.add_column(u'Results_dailybyproductiontype', 'adqcU',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqcUDir'
        db.add_column(u'Results_dailybyproductiontype', 'adqcUDir',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqcUInd'
        db.add_column(u'Results_dailybyproductiontype', 'adqcUInd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqcUAir'
        db.add_column(u'Results_dailybyproductiontype', 'adqcUAir',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqnU'
        db.add_column(u'Results_dailybyproductiontype', 'adqnU',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqnUDir'
        db.add_column(u'Results_dailybyproductiontype', 'adqnUDir',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqnUInd'
        db.add_column(u'Results_dailybyproductiontype', 'adqnUInd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.adqnUAir'
        db.add_column(u'Results_dailybyproductiontype', 'adqnUAir',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.tstnUDirFwd'
        db.add_column(u'Results_dailybyproductiontype', 'tstnUDirFwd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.tstnUIndFwd'
        db.add_column(u'Results_dailybyproductiontype', 'tstnUIndFwd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.tstnUDirBack'
        db.add_column(u'Results_dailybyproductiontype', 'tstnUDirBack',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.tstnUIndBack'
        db.add_column(u'Results_dailybyproductiontype', 'tstnUIndBack',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'DailyControls.adqnU'
        db.delete_column(u'Results_dailycontrols', 'adqnU')

        # Deleting field 'DailyControls.adqcU'
        db.delete_column(u'Results_dailycontrols', 'adqcU')


    def backwards(self, orm):
        # Adding field 'DailyByProductionType.desnUUnsp'
        db.add_column(u'Results_dailybyproductiontype', 'desnUUnsp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.descUUnsp'
        db.add_column(u'Results_dailybyproductiontype', 'descUUnsp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.descAUnsp'
        db.add_column(u'Results_dailybyproductiontype', 'descAUnsp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.firstDestructionIni'
        db.add_column(u'Results_dailybyproductiontype', 'firstDestructionIni',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.desnAUnsp'
        db.add_column(u'Results_dailybyproductiontype', 'desnAUnsp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyByProductionType.firstDestructionUnsp'
        db.add_column(u'Results_dailybyproductiontype', 'firstDestructionUnsp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'DailyByProductionType.adqcU'
        db.delete_column(u'Results_dailybyproductiontype', 'adqcU')

        # Deleting field 'DailyByProductionType.adqcUDir'
        db.delete_column(u'Results_dailybyproductiontype', 'adqcUDir')

        # Deleting field 'DailyByProductionType.adqcUInd'
        db.delete_column(u'Results_dailybyproductiontype', 'adqcUInd')

        # Deleting field 'DailyByProductionType.adqcUAir'
        db.delete_column(u'Results_dailybyproductiontype', 'adqcUAir')

        # Deleting field 'DailyByProductionType.adqnU'
        db.delete_column(u'Results_dailybyproductiontype', 'adqnU')

        # Deleting field 'DailyByProductionType.adqnUDir'
        db.delete_column(u'Results_dailybyproductiontype', 'adqnUDir')

        # Deleting field 'DailyByProductionType.adqnUInd'
        db.delete_column(u'Results_dailybyproductiontype', 'adqnUInd')

        # Deleting field 'DailyByProductionType.adqnUAir'
        db.delete_column(u'Results_dailybyproductiontype', 'adqnUAir')

        # Deleting field 'DailyByProductionType.tstnUDirFwd'
        db.delete_column(u'Results_dailybyproductiontype', 'tstnUDirFwd')

        # Deleting field 'DailyByProductionType.tstnUIndFwd'
        db.delete_column(u'Results_dailybyproductiontype', 'tstnUIndFwd')

        # Deleting field 'DailyByProductionType.tstnUDirBack'
        db.delete_column(u'Results_dailybyproductiontype', 'tstnUDirBack')

        # Deleting field 'DailyByProductionType.tstnUIndBack'
        db.delete_column(u'Results_dailybyproductiontype', 'tstnUIndBack')

        # Adding field 'DailyControls.adqnU'
        db.add_column(u'Results_dailycontrols', 'adqnU',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DailyControls.adqcU'
        db.add_column(u'Results_dailycontrols', 'adqcU',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'Results.dailybyproductiontype': {
            'Meta': {'object_name': 'DailyByProductionType'},
            'adqcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqcUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqcUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqcUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqnUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqnUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adqnUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descADet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descADirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descADirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descAIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descAIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUDet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'descURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnADet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnADirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnADirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnAIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnAIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUDet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desnURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcAClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcATest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcUClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcUTest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnAClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnATest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnUClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detnUTest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcADet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcADirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcADirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcAIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcAIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcUDet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmcURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnADet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnADirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnADirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnAIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnAIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnUDet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmnURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcAAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expcUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnAAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expnUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestruction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionDet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDestructionRing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDetection': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDetectionClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDetectionTest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstVaccination': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstVaccinationRing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcAAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infcUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnAAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnUAir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infnUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lastDetection': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lastDetectionClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lastDetectionTest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.ProductionType']", 'null': 'True', 'blank': 'True'}),
            'trcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcADirp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcAIndp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcAp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcUDirp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcUIndp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trcUp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnADir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnADirp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnAInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnAIndp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnAp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnUDir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnUDirp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnUInd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnUIndp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trnUp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdAClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdADest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdALat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdANImm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdASubc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdASusc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdAVImm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUClin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUDest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdULat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUNImm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUSubc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUSusc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tsdUVImm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcADirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcADirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcAIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcAIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUFalseNeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUFalsePos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUTrueNeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstcUTruePos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUDirBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUDirFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUFalseNeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUFalsePos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUIndBack': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUIndFwd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUTrueNeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tstnUTruePos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnAIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnARing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnUIni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacnURing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwA': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwADaysInQueue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwAMax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwAMaxDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwATimeAvg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwATimeMax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwU': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwUDaysInQueue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwUMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwUMaxDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vacwUTimeAvg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vacwUTimeMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Results.dailybyzone': {
            'Meta': {'object_name': 'DailyByZone'},
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'finalZoneArea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'finalZonePerimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maxZoneArea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'maxZoneAreaDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maxZonePerimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'maxZonePerimeterDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numSeparateAreas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.Zone']", 'null': 'True', 'blank': 'True'}),
            'zoneArea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'zonePerimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Results.dailybyzoneandproductiontype': {
            'Meta': {'object_name': 'DailyByZoneAndProductionType'},
            'animalDaysInZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.ProductionType']", 'null': 'True', 'blank': 'True'}),
            'unitDaysInZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unitsInZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.Zone']", 'null': 'True', 'blank': 'True'})
        },
        u'Results.dailycontrols': {
            'Meta': {'object_name': 'DailyControls'},
            'averagePrevalence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'costSurveillance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'costsTotal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destrAppraisal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'destrCleaning': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'destrDisposal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'destrEuthanasia': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'destrIndemnification': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'destrOccurred': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destrSubtotal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'deswADaysInQueue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswAMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswAMaxDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswATimeAvg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'deswATimeMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswUDaysInQueue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswUMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswUMaxDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deswUTimeAvg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'deswUTimeMax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detOccurred': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'detcUq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diseaseDuration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDetAInf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstDetUInf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'outbreakDuration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccOccurred': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vaccSetup': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vaccSubtotal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vaccVaccination': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Results.dailyreport': {
            'Meta': {'object_name': 'DailyReport'},
            'full_line': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sparse_dict': ('django.db.models.fields.TextField', [], {})
        },
        u'Results.unitstats': {
            'Meta': {'object_name': 'UnitStats'},
            'cumulative_destroyed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cumulative_infected': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cumulative_vaccinated': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cumulative_zone_focus': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unit': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ScenarioCreator.Unit']", 'unique': 'True'})
        },
        u'ScenarioCreator.population': {
            'Meta': {'object_name': 'Population'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_file': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'ScenarioCreator.productiontype': {
            'Meta': {'object_name': 'ProductionType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'ScenarioCreator.unit': {
            'Meta': {'object_name': 'Unit'},
            '_population': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.Population']"}),
            'days_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'days_left_in_initial_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'initial_state': ('django.db.models.fields.CharField', [], {'default': "u'S'", 'max_length': '255'}),
            'latitude': ('django_extras.db.models.fields.LatitudeField', [], {}),
            'longitude': ('django_extras.db.models.fields.LongitudeField', [], {}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ScenarioCreator.ProductionType']"}),
            'user_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'ScenarioCreator.zone': {
            'Meta': {'object_name': 'Zone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'radius': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['Results']