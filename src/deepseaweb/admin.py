from django.contrib import admin

from .models import TblCruise, TblCollector, TblCollectionEvent, TblEnvironmental
from .models import TblTaxonomy, TblLab, TblSample, TblLocation, TblTests
from .models import TblSampleTests, TblResultsBulkStableIsotope, TblResultsCompSpecAaIsotope
from .models import TblResultsFattyAcid, TblResultsFreezedry, TblResultsMercury1
from .models import TblResultsMercury2

for cls in [TblCruise, TblCollector, TblCollectionEvent, TblEnvironmental,
            TblTaxonomy, TblLab, TblSample, TblLocation, TblTests,
            TblSampleTests, TblResultsBulkStableIsotope, TblResultsCompSpecAaIsotope,
            TblResultsFattyAcid, TblResultsFreezedry, TblResultsMercury1,
            TblResultsMercury2]:
    admin.site.register(cls)
