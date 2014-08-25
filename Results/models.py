from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_hooks()
from future.builtins import object
import os
from django.db import models
import shutil
from ScenarioCreator.models import ProductionType, Zone, Unit
import re
from Settings.models import scenario_filename
from Results.output_grammar import explain
from ast import literal_eval

"""Results models explanation: The Results models are containers to capture all of the output generated by the CEngine
simulation and present it to the user broken down into 13 different tables.

Note: We are not storing cumulative values at the moment, since it can be computed.

Model Declarations: Each model creates a table in sqlite3 and a 'model' for table presentation on the GUI.  So
 each model serves double duty.  Notice that there are effectively 3 names for each field inside a model.
 1) the Python name (e.g. tsdASusc = models.) is used when constructing the object and is designed to match the CEngine output.
 2) the db_column name will show up when a user exports the DataBase.  They are at least readable explanations.
 3) verbose_name is used in the GUI for displaying Table headers.  Without this, Django would use the Python name,
 which is significantly more obscure.
 The code in scripts/Output_Table.py (.ipynb) was used to generate these name declarations.  Also, if you're reading this
 doc and you don't know about IPython Notebooks, go get IPython Notebooks."""


def printable_name(underscores_name):
    underscores_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', underscores_name).lower()  # convert from camel case
    spaced = re.sub(r'_', r' ', underscores_name)
    return spaced.title()  # capitalize


class OutputBaseModel(models.Model):
    def __iter__(self):
        for field in self._meta.fields:
            # try:
            #     value = getattr(self, field)
            # except:
            #     value = None
            yield (field.name, field)
    # This lets; you; do:
    # for field, val in myModel:
    #     print( field, val)
    class Meta(object):
        abstract = True


class DailyReport(OutputBaseModel):
    sparse_dict = models.TextField()
    full_line = models.TextField()
    # to get the dictionary object back:
    # import ast
    # ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")

    def __str__(self):
        sparse_dict = literal_eval(self.sparse_dict)
        return "iteration: %s, day: %s" % (sparse_dict['Run'], sparse_dict['Day'])


class DailyByProductionType(OutputBaseModel):
    iteration = models.IntegerField(blank=True, null=True, verbose_name=printable_name('iteration'),
        help_text='The iteration during which the outputs in this records where generated.', )
    day = models.IntegerField(blank=True, null=True, verbose_name=printable_name('day'),
        help_text='The day in this iteration during which the outputs in this records where generated.', )
    production_type = models.ForeignKey(ProductionType, blank=True, null=True, verbose_name=printable_name('production_type'),
        help_text='The identifier of the production type that these outputs apply to.', )

    desnUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUAll"))
    desnUUnsp = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUUnsp"))
    desnURing = models.IntegerField(blank=True, null=True, verbose_name=explain("desnURing"))
    desnUDet = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUDet"))
    desnUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUIni"))
    desnUDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUDirFwd"))
    desnUIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUIndFwd"))
    desnUDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUDirBack"))
    desnUIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("desnUIndBack"))
    desnAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("desnAAll"))
    desnAUnsp = models.IntegerField(blank=True, null=True, verbose_name=explain("desnAUnsp"))
    desnARing = models.IntegerField(blank=True, null=True, verbose_name=explain("desnARing"))
    desnADet = models.IntegerField(blank=True, null=True, verbose_name=explain("desnADet"))
    desnAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("desnAIni"))
    desnADirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("desnADirFwd"))
    desnAIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("desnAIndFwd"))
    desnADirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("desnADirBack"))
    desnAIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("desnAIndBack"))
    descUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("descUAll"))
    descUUnsp = models.IntegerField(blank=True, null=True, verbose_name=explain("descUUnsp"))
    descURing = models.IntegerField(blank=True, null=True, verbose_name=explain("descURing"))
    descUDet = models.IntegerField(blank=True, null=True, verbose_name=explain("descUDet"))
    descUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("descUIni"))
    descUDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("descUDirFwd"))
    descUIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("descUIndFwd"))
    descUDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("descUDirBack"))
    descUIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("descUIndBack"))
    descAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("descAAll"))
    descAUnsp = models.IntegerField(blank=True, null=True, verbose_name=explain("descAUnsp"))
    descARing = models.IntegerField(blank=True, null=True, verbose_name=explain("descARing"))
    descADet = models.IntegerField(blank=True, null=True, verbose_name=explain("descADet"))
    descAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("descAIni"))
    descADirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("descADirFwd"))
    descAIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("descAIndFwd"))
    descADirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("descADirBack"))
    descAIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("descAIndBack"))
    deswU = models.IntegerField(blank=True, null=True, verbose_name=explain("deswU"))
    deswA = models.IntegerField(blank=True, null=True, verbose_name=explain("deswA"))
    detcUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("detcUAll"))
    detcUClin = models.IntegerField(blank=True, null=True, verbose_name=explain("detcUClin"))
    detcUTest = models.IntegerField(blank=True, null=True, verbose_name=explain("detcUTest"))
    detcAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("detcAAll"))
    detcAClin = models.IntegerField(blank=True, null=True, verbose_name=explain("detcAClin"))
    detcATest = models.IntegerField(blank=True, null=True, verbose_name=explain("detcATest"))
    detnUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("detnUAll"))
    detnUClin = models.IntegerField(blank=True, null=True, verbose_name=explain("detnUClin"))
    detnUTest = models.IntegerField(blank=True, null=True, verbose_name=explain("detnUTest"))
    detnAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("detnAAll"))
    detnAClin = models.IntegerField(blank=True, null=True, verbose_name=explain("detnAClin"))
    detnATest = models.IntegerField(blank=True, null=True, verbose_name=explain("detnATest"))
    exmnUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUAll"))
    exmnURing = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnURing"))
    exmnUDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUDirFwd"))
    exmnUIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUIndFwd"))
    exmnUDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUDirBack"))
    exmnUIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUIndBack"))
    exmnUDet = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnUDet"))
    exmnAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnAAll"))
    exmnARing = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnARing"))
    exmnADirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnADirFwd"))
    exmnAIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnAIndFwd"))
    exmnADirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnADirBack"))
    exmnAIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnAIndBack"))
    exmnADet = models.IntegerField(blank=True, null=True, verbose_name=explain("exmnADet"))
    exmcUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUAll"))
    exmcURing = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcURing"))
    exmcUDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUDirFwd"))
    exmcUIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUIndFwd"))
    exmcUDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUDirBack"))
    exmcUIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUIndBack"))
    exmcUDet = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcUDet"))
    exmcAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcAAll"))
    exmcARing = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcARing"))
    exmcADirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcADirFwd"))
    exmcAIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcAIndFwd"))
    exmcADirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcADirBack"))
    exmcAIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcAIndBack"))
    exmcADet = models.IntegerField(blank=True, null=True, verbose_name=explain("exmcADet"))
    expcU = models.IntegerField(blank=True, null=True, verbose_name=explain("expcU"))
    expcUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("expcUDir"))
    expcUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("expcUInd"))
    expcUAir = models.IntegerField(blank=True, null=True, verbose_name=explain("expcUAir"))
    expcA = models.IntegerField(blank=True, null=True, verbose_name=explain("expcA"))
    expcADir = models.IntegerField(blank=True, null=True, verbose_name=explain("expcADir"))
    expcAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("expcAInd"))
    expcAAir = models.IntegerField(blank=True, null=True, verbose_name=explain("expcAAir"))
    expnU = models.IntegerField(blank=True, null=True, verbose_name=explain("expnU"))
    expnUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("expnUDir"))
    expnUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("expnUInd"))
    expnUAir = models.IntegerField(blank=True, null=True, verbose_name=explain("expnUAir"))
    expnA = models.IntegerField(blank=True, null=True, verbose_name=explain("expnA"))
    expnADir = models.IntegerField(blank=True, null=True, verbose_name=explain("expnADir"))
    expnAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("expnAInd"))
    expnAAir = models.IntegerField(blank=True, null=True, verbose_name=explain("expnAAir"))
    firstDestruction = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestruction"))
    firstDestructionUnsp = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionUnsp"))
    firstDestructionRing = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionRing"))
    firstDestructionDet = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionDet"))
    firstDestructionIni = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionIni"))
    firstDestructionDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionDirFwd"))
    firstDestructionIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionIndFwd"))
    firstDestructionDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionDirBack"))
    firstDestructionIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDestructionIndBack"))
    firstDetection = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDetection"))
    firstDetectionClin = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDetectionClin"))
    firstDetectionTest = models.IntegerField(blank=True, null=True, verbose_name=explain("firstDetectionTest"))
    firstVaccination = models.IntegerField(blank=True, null=True, verbose_name=explain("firstVaccination"))
    firstVaccinationRing = models.IntegerField(blank=True, null=True, verbose_name=explain("firstVaccinationRing"))
    infcU = models.IntegerField(blank=True, null=True, verbose_name=explain("infcU"))
    infcUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("infcUIni"))
    infcUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("infcUDir"))
    infcUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("infcUInd"))
    infcUAir = models.IntegerField(blank=True, null=True, verbose_name=explain("infcUAir"))
    infcA = models.IntegerField(blank=True, null=True, verbose_name=explain("infcA"))
    infcAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("infcAIni"))
    infcADir = models.IntegerField(blank=True, null=True, verbose_name=explain("infcADir"))
    infcAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("infcAInd"))
    infcAAir = models.IntegerField(blank=True, null=True, verbose_name=explain("infcAAir"))
    infnU = models.IntegerField(blank=True, null=True, verbose_name=explain("infnU"))
    infnUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("infnUIni"))
    infnUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("infnUDir"))
    infnUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("infnUInd"))
    infnUAir = models.IntegerField(blank=True, null=True, verbose_name=explain("infnUAir"))
    infnA = models.IntegerField(blank=True, null=True, verbose_name=explain("infnA"))
    infnAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("infnAIni"))
    infnADir = models.IntegerField(blank=True, null=True, verbose_name=explain("infnADir"))
    infnAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("infnAInd"))
    infnAAir = models.IntegerField(blank=True, null=True, verbose_name=explain("infnAAir"))
    lastDetection = models.IntegerField(blank=True, null=True, verbose_name=explain("lastDetection"))
    lastDetectionClin = models.IntegerField(blank=True, null=True, verbose_name=explain("lastDetectionClin"))
    lastDetectionTest = models.IntegerField(blank=True, null=True, verbose_name=explain("lastDetectionTest"))
    trnUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUAll"))
    trnUAllp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUAllp"))
    trnUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUDir"))
    trnUDirp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUDirp"))
    trnUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUInd"))
    trnUIndp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnUIndp"))
    trnAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("trnAAll"))
    trnAAllp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnAAllp"))
    trnADir = models.IntegerField(blank=True, null=True, verbose_name=explain("trnADir"))
    trnADirp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnADirp"))
    trnAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("trnAInd"))
    trnAIndp = models.IntegerField(blank=True, null=True, verbose_name=explain("trnAIndp"))
    trcUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUAll"))
    trcUAllp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUAllp"))
    trcUDir = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUDir"))
    trcUDirp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUDirp"))
    trcUInd = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUInd"))
    trcUIndp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcUIndp"))
    trcAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("trcAAll"))
    trcAAllp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcAAllp"))
    trcADir = models.IntegerField(blank=True, null=True, verbose_name=explain("trcADir"))
    trcADirp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcADirp"))
    trcAInd = models.IntegerField(blank=True, null=True, verbose_name=explain("trcAInd"))
    trcAIndp = models.IntegerField(blank=True, null=True, verbose_name=explain("trcAIndp"))
    tsdUSusc = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUSusc"))
    tsdULat = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdULat"))
    tsdUSubc = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUSubc"))
    tsdUClin = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUClin"))
    tsdUNImm = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUNImm"))
    tsdUVImm = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUVImm"))
    tsdUDest = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdUDest"))
    tsdASusc = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdASusc"))
    tsdALat = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdALat"))
    tsdASubc = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdASubc"))
    tsdAClin = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdAClin"))
    tsdANImm = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdANImm"))
    tsdAVImm = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdAVImm"))
    tsdADest = models.IntegerField(blank=True, null=True, verbose_name=explain("tsdADest"))
    tstcAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcAAll"))
    tstcADirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcADirFwd"))
    tstcAIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcAIndFwd"))
    tstcADirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcADirBack"))
    tstcAIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcAIndBack"))
    tstcUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUAll"))
    tstcUDirFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUDirFwd"))
    tstcUIndFwd = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUIndFwd"))
    tstcUDirBack = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUDirBack"))
    tstcUIndBack = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUIndBack"))
    tstcUTruePos = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUTruePos"))
    tstcUFalsePos = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUFalsePos"))
    tstcUTrueNeg = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUTrueNeg"))
    tstcUFalseNeg = models.IntegerField(blank=True, null=True, verbose_name=explain("tstcUFalseNeg"))
    tstnUTruePos = models.IntegerField(blank=True, null=True, verbose_name=explain("tstnUTruePos"))
    tstnUFalsePos = models.IntegerField(blank=True, null=True, verbose_name=explain("tstnUFalsePos"))
    tstnUTrueNeg = models.IntegerField(blank=True, null=True, verbose_name=explain("tstnUTrueNeg"))
    tstnUFalseNeg = models.IntegerField(blank=True, null=True, verbose_name=explain("tstnUFalseNeg"))
    vaccUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccUAll"))
    vaccUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccUIni"))
    vaccURing = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccURing"))
    vaccAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccAAll"))
    vaccAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccAIni"))
    vaccARing = models.IntegerField(blank=True, null=True, verbose_name=explain("vaccARing"))
    vacnUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnUAll"))
    vacnUIni = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnUIni"))
    vacnURing = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnURing"))
    vacnAAll = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnAAll"))
    vacnAIni = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnAIni"))
    vacnARing = models.IntegerField(blank=True, null=True, verbose_name=explain("vacnARing"))
    vacwUAll = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwUAll"))
    vacwUMax = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwUMax"))
    vacwUMaxDay = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwUMaxDay"))
    vacwUTimeMax = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwUTimeMax"))
    vacwUTimeAvg = models.FloatField(blank=True, null=True, verbose_name=explain("vacwUTimeAvg"))
    vacwUDaysInQueue = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwUDaysInQueue"))
    vacwAAll = models.FloatField(blank=True, null=True, verbose_name=explain("vacwAAll"))
    vacwAMax = models.FloatField(blank=True, null=True, verbose_name=explain("vacwAMax"))
    vacwAMaxDay = models.IntegerField(blank=True, null=True, verbose_name=explain("vacwAMaxDay"))
    vacwATimeMax = models.FloatField(blank=True, null=True, verbose_name=explain("vacwATimeMax"))
    vacwATimeAvg = models.FloatField(blank=True, null=True, verbose_name=explain("vacwATimeAvg"))
    vacwADaysInQueue = models.FloatField(blank=True, null=True, verbose_name=explain("vacwADaysInQueue"))


#####END DailyByProductionType######

#####BEGIN DailyByZoneAndProductionType######


class DailyByZoneAndProductionType(OutputBaseModel):
    iteration = models.IntegerField(blank=True, null=True, verbose_name=printable_name('iteration'),
        help_text='The iteration during which the outputs in this records where generated.', )
    day = models.IntegerField(blank=True, null=True, verbose_name=printable_name('day'),
        help_text='The day in this iteration during which the outputs in this records where generated.', )
    production_type = models.ForeignKey(ProductionType, blank=True, null=True, verbose_name=printable_name('production_type'),
        help_text='The identifier of the production type that these outputs apply to.', )
    zone = models.ForeignKey(Zone, blank=True, null=True, verbose_name=printable_name('zone'),
        help_text='The identifier of the zone that these outputs apply to.', )

    unitsInZone      = models.IntegerField(blank=True, null=True, verbose_name=printable_name('unitsInZone'))
    unitDaysInZone   = models.IntegerField(blank=True, null=True, verbose_name=printable_name('unitDaysInZone'))
    animalDaysInZone = models.IntegerField(blank=True, null=True, verbose_name=printable_name('animalDaysInZone'))

    def __str__(self):
        return "%i, %i: %s and %s" % (self.iteration, self.day, self.production_type or "All Types", self.zone or "Background")


class DailyByZone(OutputBaseModel):
    iteration = models.IntegerField(blank=True, null=True, verbose_name=printable_name('iteration'),
        help_text='The iteration during which the outputs in this records where generated.', )
    day = models.IntegerField(blank=True, null=True, verbose_name=printable_name('day'),
        help_text='The day in this iteration during which the outputs in this records where generated.', )
    zone = models.ForeignKey(Zone, blank=True, null=True, verbose_name=printable_name('zone'),
        help_text='The identifier of the zone that these outputs apply to.', )

    zoneArea            = models.FloatField(blank=True, null=True, verbose_name=printable_name('zoneArea'))
    maxZoneArea         = models.FloatField(blank=True, null=True, verbose_name=printable_name('maxZoneArea'))
    maxZoneAreaDay      = models.IntegerField(blank=True, null=True, verbose_name=printable_name('maxZoneAreaDay'))
    zonePerimeter       = models.FloatField(blank=True, null=True, verbose_name=printable_name('zonePerimeter'))
    maxZonePerimeter    = models.FloatField(blank=True, null=True, verbose_name=printable_name('maxZonePerimeter'))
    maxZonePerimeterDay = models.IntegerField(blank=True, null=True, verbose_name=printable_name('maxZonePerimeterDay'))
    finalZoneArea       = models.FloatField(blank=True, null=True, verbose_name=printable_name('finalZoneArea'))
    finalZonePerimeter  = models.FloatField(blank=True, null=True, verbose_name=printable_name('finalZonePerimeter'))
    numSeparateAreas  = models.IntegerField(blank=True, null=True, verbose_name=printable_name('number of separate areas'))


class DailyControls(OutputBaseModel):
    iteration = models.IntegerField(blank=True, null=True, verbose_name=printable_name('iteration'),
        help_text='The iteration during which the outputs in this records where generated.', )
    day = models.IntegerField(blank=True, null=True, verbose_name=printable_name('day'),
        help_text='The day in this iteration during which the outputs in this records where generated.', )

    diseaseDuration      = models.IntegerField(blank=True, null=True, verbose_name=printable_name('diseaseDuration'))
    adqnUAll             = models.IntegerField(blank=True, null=True, verbose_name=printable_name('New Units Adequately Exposed'))
    adqcUAll             = models.IntegerField(blank=True, null=True, verbose_name=printable_name('Cumulative Units Adequately Exposed'))
    detOccurred          = models.IntegerField(blank=True, null=True, verbose_name=printable_name('detOccurred'))
    costSurveillance     = models.FloatField(blank=True, null=True, verbose_name=printable_name('costSurveillance'))
    vaccOccurred         = models.IntegerField(blank=True, null=True, verbose_name=printable_name('vaccOccurred'))
    vaccSetup            = models.FloatField(blank=True, null=True, verbose_name=printable_name('vaccSetup'))
    vaccVaccination      = models.FloatField(blank=True, null=True, verbose_name=printable_name('vaccVaccination'))
    vaccSubtotal         = models.FloatField(blank=True, null=True, verbose_name=printable_name('vaccSubtotal'))
    destrOccurred        = models.IntegerField(blank=True, null=True, verbose_name=printable_name('destrOccurred'))

    deswUMax = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Units Max")
    deswUMaxDay = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Units Day with Max")
    deswUTimeMax = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Units Max Time")
    deswUTimeAvg = models.FloatField(blank=True, null=True, verbose_name="Destruction Wait Time Units Average Time")
    deswUDaysInQueue = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Units Days in Queue")
    deswAMax = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Animals Max")
    deswAMaxDay = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Animals Day with Max")
    deswATimeMax = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Animals Max Time")
    deswATimeAvg = models.FloatField(blank=True, null=True, verbose_name="Destruction Wait Time Animals Average Time")
    deswADaysInQueue = models.IntegerField(blank=True, null=True, verbose_name="Destruction Wait Time Animals Days in Queue")

    destrAppraisal       = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrAppraisal'))
    destrEuthanasia      = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrEuthanasia'))
    destrIndemnification = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrIndemnification'))
    destrDisposal        = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrDisposal'))
    destrCleaning        = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrCleaning'))
    destrSubtotal        = models.FloatField(blank=True, null=True, verbose_name=printable_name('destrSubtotal'))
    outbreakDuration     = models.IntegerField(blank=True, null=True, verbose_name=printable_name('outbreakDuration'))
    costsTotal           = models.FloatField(blank=True, null=True, verbose_name=printable_name('costsTotal'))
    firstDetUInfAll      = models.IntegerField(blank=True, null=True, verbose_name=printable_name('Units Infected at First Detection'))
    firstDetAInfAll      = models.IntegerField(blank=True, null=True, verbose_name=printable_name('Animals Infected at First Detection'))
    ratio                = models.IntegerField(blank=True, null=True, verbose_name=printable_name('ratio'))
    averagePrevalence   = models.IntegerField(blank=True, null=True, verbose_name=printable_name('averagePrevalence'))
    detcUqAll            = models.IntegerField(blank=True, null=True, verbose_name=printable_name('detcUqAll'))


class UnitStats(OutputBaseModel):
    """Model for holding Unit related output primarily for the Results map Issue # 211.
    If we run into database contention issues, try switching the database mode to http://www.sqlite.org/draft/wal.html"""
    unit = models.OneToOneField(Unit,
        help_text='Pointer back to the input Unit (lat/long) these stats are for.')
    cumulative_infected = models.PositiveIntegerField(default=0,
        help_text='The total number of iterations in which this unit became infected.', )
    cumulative_zone_focus = models.PositiveIntegerField(default=0,
        help_text='The total number of iterations in which this unit was a zone focus.', )
    cumulative_destroyed = models.PositiveIntegerField(default=0,
        help_text='The total number of iterations in which this unit was destroyed.', )
    cumulative_vaccinated = models.PositiveIntegerField(default=0,
        help_text='The total number of iterations in which this unit was vaccinated.', )


def delete_all_outputs():
    output_models = [DailyControls, DailyReport, DailyByZone, DailyByProductionType, DailyByZoneAndProductionType, UnitStats]
    for model in output_models:
        model.objects.all().delete()
    scenario_folder = scenario_filename()
    if scenario_folder != '':
        try:
            shutil.rmtree(os.path.join('workspace', scenario_folder))
        except:
            pass  # because the folder doesn't exist (which is fine)
