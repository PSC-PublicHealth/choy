from django.contrib import admin
from django import forms 

from .models import TblCruise, TblCollector, TblCollectionEvent, TblEnvironmental
from .models import TblTaxonomy, TblLab, TblSample, TblLocation, TblTests
from .models import TblSampleTests, TblResultsBulkStableIsotope, TblResultsCompSpecAaIsotope
from .models import TblResultsFattyAcid, TblResultsFreezedry, TblResultsMercury1
from .models import TblResultsMercury2, TblOriginType, TblLengthType

for cls in [
#            TblCruise,
#            TblCollector,
#            TblCollectionEvent,
#            TblEnvironmental,
#            TblTaxonomy,
#            TblLab,
#            TblSample,
#            TblLocation,
            TblTests,
            TblSampleTests,
            TblResultsBulkStableIsotope,
            TblResultsCompSpecAaIsotope,
            TblResultsFattyAcid,
            TblResultsFreezedry,
            TblResultsMercury1,
            TblResultsMercury2,
#            TblOriginType,
#            TblLengthType
            ]:
    admin.site.register(cls)


class CruiseAdmin(admin.ModelAdmin):

    list_display = ('cruise_name','cruise_start','cruise_end','region','vessel','chief_scientist','description')

    fields = (
            'cruise_name',
            ('cruise_start','cruise_end'),
            'vessel',
            'region',
            'chief_scientist',
            'description'
            )


admin.site.register(TblCruise,CruiseAdmin)


class CollectorAdmin(admin.ModelAdmin):

    list_display = ('collector_type', 'description')

admin.site.register(TblCollector, CollectorAdmin)


class CollectionEventAdmin(admin.ModelAdmin):

    list_display = ('collection_event_id','cruise_id','collector_id','collection_event_date','description')

admin.site.register(TblCollectionEvent,CollectionEventAdmin)


class OriginTypeAdmin(admin.ModelAdmin):

    list_display = ('origin_type_id','origin_type_label')

admin.site.register(TblOriginType,OriginTypeAdmin)


class EnvironmentalAdmin(admin.ModelAdmin):
    list_display = (
            'environmental_id','collection_event_id','environmental_datetime',
            'sampler','depth_discrete','depth_min','depth_max','latitude','longitude','notes'
            )
    fields = (
            ('collection_event_id','environmental_datetime'),
            'sampler',
            ('depth_discrete','depth_min','depth_max'),
            ('latitude','longitude'),
            'notes'
             )

admin.site.register(TblEnvironmental,EnvironmentalAdmin)


#class Admin(admin.ModelAdmin):
#
#    list_display = (
#            ''
#            )
#
#admin.site.register(Tbl,Admin)


class TaxonomyAdmin(admin.ModelAdmin):

    list_display = (
            'taxonomy_id','category','animal','phylum','subphylum','class_field',
            'order_field','family','genus','species'
            )

admin.site.register(TblTaxonomy,TaxonomyAdmin)


class LabAdmin(admin.ModelAdmin):

    list_display = (
            'lab_id','lab_name','address','contact_name','contact_email','contact_phone'
            )

admin.site.register(TblLab,LabAdmin)


class LocationAdmin(admin.ModelAdmin):

    list_display = (
            'location_id','sample_id','institution','location'
            )

admin.site.register(TblLocation,LocationAdmin)


class LengthTypeAdmin(admin.ModelAdmin):

    list_display = ('length_type_id','length_type_label')

admin.site.register(TblLengthType,LengthTypeAdmin)


class SampleAdmin(admin.ModelAdmin):

    list_display = (
            'sample_id','AC_sample_id','environmental_id','taxonomy_id',
            'origin_id','origin_type','processing_id',
            'length1_mm','length1_type','length2_mm','length2_type','wet_whole_mass_g',
            'n_individuals','tissue_type','remaining_mass_g'
            )
    fields = (
            'AC_sample_id',
            'environmental_id',
            'taxonomy_id',
            ('origin_id','origin_type'),
            'processing_id',
            ('length1_mm','length1_type'),
            ('length2_mm','length2_type'),
            ('wet_whole_mass_g','remaining_mass_g'),
            'n_individuals',
            'tissue_type',
            )

    def add_view(self, request, form_url='', extra_context=None):
        """ Customized add_view prepopulates admin fields with last created values for
        select fields
        """
        data = request.GET.copy()

        origin_types = TblOriginType.objects.all()
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


