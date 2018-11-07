from django.contrib import admin
from django import forms 

from .models import TblCruise, TblCollector, TblCollectionEvent, TblEnvironmental
from .models import TblTaxonomy, TblLab, TblSample, TblLocation, TblTests
from .models import TblSampleTests, TblResultsBulkStableIsotope, TblResultsCompSpecAaIsotope
from .models import TblResultsFattyAcid, TblResultsFreezedry, TblResultsMercury1
from .models import TblResultsMercury2, TblOriginTypes

for cls in [
            TblCruise,
            TblCollector,
            TblCollectionEvent,
            TblEnvironmental,
            TblTaxonomy,
            TblLab,
#            TblSample,
            TblLocation,
            TblTests,
            TblSampleTests,
            TblResultsBulkStableIsotope,
            TblResultsCompSpecAaIsotope,
            TblResultsFattyAcid,
            TblResultsFreezedry,
            TblResultsMercury1,
            TblResultsMercury2,
            TblOriginTypes
            ]:
    admin.site.register(cls)

class SampleAdmin(admin.ModelAdmin):

    list_display = (
            'sampleid','acsampleid','environmentalid','taxonomyid',
            'originid','origin_type','processingid',
            'length1_mm','length1_type','length2_mm','length2_type','wet_whole_mass_g',
            'n_individuals','tissuetype','remaining_mass_g'
            )
    fields = (
            ('sampleid','acsampleid'),
            'environmentalid',
            'taxonomyid',
            ('originid','origin_type'),
            'processingid',
            ('length1_mm','length1_type'),
            ('length2_mm','length2_type'),
            ('wet_whole_mass_g','remaining_mass_g'),
            'n_individuals',
            'tissuetype',
            )
    def add_view(self, request, form_url='', extra_context=None):
        """ Customized add_view prepopulates admin fields with last created values for
        select fields
        """
        data = request.GET.copy()

        origin_types = TblOriginTypes.objects.all()
        if len(origin_types) > 0:
            data['origin_type'] = origin_types[len(origin_types)-1]

        environmental_ids = TblEnvironmental.objects.all()
        if len(environmental_ids) > 0:
            data['environmentalid'] = environmental_ids[len(environmental_ids)-1]
        
        taxonomy_ids = TblTaxonomy.objects.all()
        if len(taxonomy_ids) > 0:
            data['taxonomyid'] = taxonomy_ids[len(taxonomy_ids)-1]

        request.GET = data
        return super().add_view(request, form_url=form_url, extra_context=extra_context)


admin.site.register(TblSample, SampleAdmin)
