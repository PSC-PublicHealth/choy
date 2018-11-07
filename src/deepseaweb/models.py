# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblCruise(models.Model):
    cruise_id = models.AutoField(db_column='CruiseID', primary_key=True) 
    cruise_name = models.CharField(db_column='CruiseName', null=False, max_length=45)
    cruise_start = models.DateField(db_column='CruiseStart', blank=True, null=True)
    cruise_end = models.DateField(db_column='CruiseEnd', blank=True, null=True)
    vessel = models.CharField(db_column='Vessel',blank=True,null=True, max_length=45)
    region = models.CharField(db_column='Region',blank=True,null=True, max_length=45)
    chief_scientist = models.CharField(db_column='ChiefScientist',blank=True, null=True, max_length=45)
    description = models.CharField(db_column='Description',blank=True, null=True, max_length=100)

    def __str__(self):
        return '%s (%d)' % (self.cruise_name, self.cruise_id)

    class Meta:
        managed = True
        db_table = 'tbl_cruise'


class TblCollector(models.Model):
    collector_id = models.AutoField(db_column='CollectorID', primary_key=True)
    collector_type = models.CharField(db_column='CollectorType', blank=True, null=True, max_length=45)
    description = models.CharField(db_column='Description',blank=True, null=True, max_length=100)

    def __str__(self):
        return '%s' % (self.collector_type)

    class Meta:
        managed = True
        db_table = 'tbl_collector'


class TblCollectionEvent(models.Model):
    collection_event_id = models.CharField(db_column='CollEventID',primary_key=True, max_length=45)
    cruise_id = models.ForeignKey(TblCruise, models.DO_NOTHING, db_column='CruiseID')
    collector_id = models.ForeignKey(TblCollector, models.DO_NOTHING, db_column='CollectorID')
    collection_event_date = models.DateField(db_column='CollEventDate', blank=True)
    description = models.CharField(db_column='Description',blank=True, null=True, max_length=100)

    def __str__(self):
        return '%s (%s)' % (self.collection_event_id, self.collection_event_date)

    class Meta:
        managed = True
        db_table = 'tbl_collection_event'


class TblEnvironmental(models.Model):
    environmental_id = models.AutoField(db_column='EnvironmentalID',primary_key=True)
    collection_event_id = models.ForeignKey(TblCollectionEvent, models.DO_NOTHING, db_column='CollEventID')
    environmental_datetime = models.DateTimeField(db_column='DateTime24-GMT',blank=True, null=True)
    sampler = models.CharField(db_column='Sampler',blank=True, null=True, max_length=25)
    depth_discrete = models.IntegerField(db_column='DepthDiscrete',blank=True, null=True)
    depth_min = models.IntegerField(db_column='DepthMin',blank=True, null=True)
    depth_max = models.IntegerField(db_column='DepthMax',blank=True, null=True)
    latitude = models.DecimalField(db_column='Latitude',max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(db_column='Longitude',max_digits=9, decimal_places=6, blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s,%s)' % (self.collection_event_id, self.environmental_datetime.time(), max([x for x in [self.depth_discrete,self.depth_max,self.depth_min] if x is not None]))

    class Meta:
        managed = True
        db_table = 'tbl_environmental'


class TblTaxonomy(models.Model):
    taxonomy_id = models.CharField(db_column='TaxonomyID', primary_key=True, max_length=45)  
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  
    animal = models.CharField(db_column='Animal',max_length=20, blank=True, null=True)
    phylum = models.CharField(db_column='Phylum', max_length=20, blank=True, null=True)  
    subphylum = models.CharField(db_column='Subphylum', max_length=20, blank=True, null=True)  
    class_field = models.CharField(db_column='Class', max_length=20, blank=True, null=True)   
    order_field = models.CharField(db_column='Order_', max_length=20, blank=True, null=True)  
    suborder = models.CharField(db_column='SubOrder', max_length=40, blank=True, null=True)
    family = models.CharField(db_column='Family', max_length=50, blank=True, null=True)  
    genus = models.CharField(db_column='Genus', max_length=50, blank=True, null=True)  
    species = models.CharField(db_column='Species', max_length=40, blank=True, null=True)  

    def __str__(self):
        return '%s' % (self.taxonomy_id)

    class Meta:
        managed = True
        db_table = 'tbl_taxonomy'


class TblLab(models.Model):
    lab_id = models.AutoField(db_column='LabID', primary_key=True)  
    lab_name = models.CharField(db_column='LabName', max_length=30)  
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  
    contact_name = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  
    contact_email = models.CharField(db_column='ContactEmail', max_length=30, blank=True, null=True)  
    contact_phone = models.CharField(db_column='ContactPhone', max_length=12, blank=True, null=True)  

    def __str__(self):
        return '%s' % (self.lab_name)

    class Meta:
        managed = True
        db_table = 'tbl_lab'


class TblOriginType(models.Model):
    origin_type_id=models.AutoField(db_column='OriginID', primary_key=True)
    origin_type_label=models.CharField(db_column='SubsampleType', max_length=20)

    def __str__(self):
        return '%s' % (self.origin_type_label)

    class Meta:
        managed = True
        db_table = 'tbl_origin_type'

class TblLengthType(models.Model):
    length_type_id=models.AutoField(db_column='LengthTypeID',primary_key=True)
    length_type_label=models.CharField(db_column='LengthTypeLabel',max_length=20)

    def __str__(self):
        return '%s' % (self.length_type_label)

    class Meta:
        managed = True
        db_table = 'tbl_length type'

class TblSample(models.Model):
    sample_id = models.AutoField(db_column='SampleID', primary_key=True)  
    AC_sample_id = models.CharField(db_column='ACSampleID', max_length=45, blank=True, null=True)  
    environmental_id = models.ForeignKey('TblEnvironmental',models.CASCADE, db_column='EnvironmentalID')
    taxonomy_id = models.ForeignKey('TblTaxonomy', models.DO_NOTHING, db_column='TaxonomyID')  
    origin_id = models.IntegerField(db_column='SampleOriginID', default=0, blank=True, null=True) #if subsampled, use original sample id
    origin_type = models.ForeignKey('TblOriginType', models.DO_NOTHING, db_column='OriginID', default=0)
    processing_id = models.CharField(db_column='ProcessingID', max_length=20, blank=True, null=True) #originally DryLogID
    length1_mm = models.FloatField(db_column='Length1_MM', blank=True, null=True)  
    length1_type = models.ForeignKey('TblLengthType',models.DO_NOTHING, db_column='Length1_type', max_length=20, related_name='%(class)s_L1_type')
    length2_mm = models.FloatField(db_column='Length2_MM', blank=True, null=True) 
    length2_type = models.ForeignKey('TblLengthType',models.DO_NOTHING, db_column='Length2_type', max_length=20, related_name='%(class)s_L2_type')
    wet_whole_mass_g = models.FloatField(db_column='Wet_Whole_Mass_G', blank=True, null=True)  
    n_individuals = models.IntegerField(db_column='N_Individuals',default=1)
    tissue_type = models.CharField(db_column='TissueType', max_length=30, blank=True, null=True)
    remaining_mass_g = models.FloatField(db_column='Remaining_Mass_G',blank=True, null=True)
    

    def __str__(self):
        return '%s' % (self.AC_sample_id)

    class Meta:
        managed = True
        db_table = 'tbl_sample'


class TblLocation(models.Model):
    location_id = models.AutoField(db_column='LocationID',primary_key=True)
    sample_id = models.ForeignKey('TblSample',models.DO_NOTHING, db_column='SampleID')
    institution = models.CharField(db_column='Institution', max_length=50)
    location = models.CharField(db_column='Location', max_length=50)

    def __str__(self):
        return '%s/%s' % (self.institution, self.location)

    class Meta:
        managed = True
        db_table = 'tbl_location'  


class TblTests(models.Model):
    test_id = models.AutoField(db_column='TestID', primary_key=True)  
    test_type = models.CharField(db_column='TestType', max_length=20)  
    result_table = models.CharField(db_column='ResultTable', max_length=20)  
    lab_id = models.ForeignKey(TblLab, models.DO_NOTHING, db_column='LabID')  

    def __str__(self):
        return '%s' % (self.test_type)

    class Meta:
        managed = True
        db_table = 'tbl_tests'


class TblSampleTests(models.Model):
    sample_test_id = models.AutoField(db_column='SampleTestID', primary_key=True)  
    sample_id = models.ForeignKey(TblSample, models.DO_NOTHING, db_column='SampleID')  
    test_id = models.ForeignKey('TblTests', models.DO_NOTHING, db_column='TestID')  
    result_id = models.IntegerField(db_column='ResultID', blank=True, null=True)  
    test_sent = models.DateField(db_column='TestSent', blank=True, null=True)  
    result_recd = models.DateField(db_column='ResultRecd', blank=True, null=True)  
    qaqc = models.BooleanField(db_column='QAQC', default=False)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_sample_tests'


class TblResultsBulkStableIsotope(models.Model):
    r6id = models.AutoField(db_column='R6ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysis_date = models.DateField(db_column='AnalysisDate')  
    analyzed_by = models.CharField(db_column='AnalyzedBy', max_length=30, blank=True, null=True)  
    He_dilution = models.CharField(db_column='HeDilution', max_length=30, blank=True, null=True)  
    notes = models.TextField(db_column='Notes', blank=True, null=True)  
    EA_mass_mg = models.FloatField(db_column='EA_mass_mg', blank=True, null=True)  
    n_ug = models.FloatField(db_column='N_ug', blank=True, null=True)  
    d15n = models.FloatField(db_column='d15N', blank=True, null=True)  
    c_ug = models.FloatField(db_column='C_ug', blank=True, null=True)  
    d13c = models.FloatField(db_column='d13C', blank=True, null=True)  
    acidified = models.BooleanField(db_column='Acidified', default=False)
#    molarcn = models.FloatField(db_column='MolarCN',default=(c_ug/10^6/12.01)/(n_ug/10^6/14.01))
    molar_CN = models.FloatField(db_column='MolarCN', blank=True, null=True)
    comments = models.TextField(db_column='Comments', blank=True, null=True)  
    replicates = models.BooleanField(db_column='Replicates',default=False)

    class Meta:
        managed = True
        db_table = 'tbl_results_bulk_stable_isotope'


class TblResultsCompSpecAaIsotope(models.Model):
    r5id = models.AutoField(db_column='R5ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisd_ate = models.DateField(db_column='AnalysisDate')  
    run_num = models.CharField(db_column='RunNum', max_length=20)  
    amino_acid = models.CharField(db_column='AminoAcid', max_length=20, blank=True, null=True)  
    ea_irms = models.FloatField(db_column='EA-IRMS', blank=True, null=True) 
    rt = models.FloatField(db_column='RT', blank=True, null=True)  
    peak = models.IntegerField(db_column='Peak', blank=True, null=True)  
    rt2 = models.FloatField(db_column='RT2', blank=True, null=True)  
    area = models.FloatField(db_column='Area', blank=True, null=True)  
    d15n_un = models.FloatField(db_column='d15N_un', blank=True, null=True)  
    d15n_std = models.FloatField(db_column='d15N_std', blank=True, null=True)  
    d15n_reg = models.FloatField(db_column='d15N_reg', blank=True, null=True)  
    standard = models.CharField(db_column='Standard', max_length=30, blank=True, null=True)  
    vial_id = models.CharField(db_column='VialID', max_length=20, blank=True, null=True)  
    sample_weight = models.FloatField(db_column='SampleWeight', blank=True, null=True)  
    ea_ul = models.IntegerField(db_column='EA_uL', blank=True, null=True)  
    injection_volume = models.FloatField(db_column='InjectionVolume', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_comp_spec_AA_isotope'


class TblResultsFattyAcid(models.Model):
    r4id = models.AutoField(db_column='R4ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysis_date = models.DateField(db_column='AnalysisDate')  
    csiro_id = models.TextField(db_column='CSIRO_ID')  
    noaa_ll_specimenid = models.TextField(db_column='NOAA_LL_SpecimenID')  
    tissue_type = models.CharField(db_column='TissueType', max_length=20, blank=True, null=True)  
    tissue_location = models.CharField(db_column='TissueLocation', max_length=20, blank=True, null=True)  
    catch_date = models.DateField(db_column='CatchDate', blank=True, null=True)  
    fork_length_cm = models.FloatField(db_column='Forklength_cm', blank=True, null=True)  
    whole_mass_g = models.FloatField(db_column='WholeMass_g', blank=True, null=True)  
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  
    dry_mass_g = models.FloatField(db_column='DryMass_g', blank=True, null=True)  
    capless_vial_and_lipid_g = models.FloatField(db_column='CaplessVialAndLipid_g', blank=True, null=True)  
    capless_vial_g = models.FloatField(db_column='CaplessVial_g', blank=True, null=True)  
    lipid_mass_g = models.FloatField(db_column='LipidMass_g', blank=True, null=True)  
    lipid_mass_mg = models.FloatField(db_column='LipidMass_mg', blank=True, null=True)  
    c19_internal_standard_added_ul = models.IntegerField(db_column='C19_Internal_Standard_Added_ul', blank=True, null=True)  
    percent_lipid_drywt = models.FloatField(db_column='PercentLipid_drywt', blank=True, null=True)  
    methylation_ul = models.IntegerField(db_column='Methylation_ul', blank=True, null=True)  
    tl_volume_ul = models.IntegerField(db_column='TL_Volume_ul', blank=True, null=True)  
    percent_lipid_drywt_reweigh = models.FloatField(db_column='PercentLipid_drywt_reweigh', blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_fattyacid'


class TblResultsFreezedry(models.Model):
    r3id = models.AutoField(db_column='R3ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysis_date = models.DateField(db_column='AnalysisDate')  
    family = models.TextField(db_column='Family', blank=True, null=True)  
    genus = models.TextField(db_column='Genus', blank=True, null=True)  
    species = models.TextField(db_column='Species', blank=True, null=True)  
    counts = models.IntegerField(db_column='Counts', blank=True, null=True)  
    length1_type = models.ForeignKey('TblLengthType',models.DO_NOTHING, db_column='Length1_type', max_length=20)
    length1_type = models.ForeignKey('TblLengthType',models.DO_NOTHING, db_column='Length1_type', max_length=20, related_name='%(class)s_L1_type')
    length1_mm = models.IntegerField(db_column='Length1_mm', blank=True, null=True)  
    length2_type = models.ForeignKey('TblLengthType',models.DO_NOTHING, db_column='Length2_type', max_length=20, related_name='%(class)s_L2_type')
    length2_mm = models.IntegerField(db_column='Length2_mm', blank=True, null=True)  
    whole_wet_mass = models.IntegerField(db_column='WholeWetMass', blank=True, null=True)  
    wet_remaining = models.TextField(db_column='WetRemaining', blank=True, null=True)  
    vessel = models.FloatField(db_column='Vessel', blank=True, null=True)  
    vessel_and_wet = models.FloatField(db_column='VesselAndWet', blank=True, null=True)  
    vessel_and_dry = models.FloatField(db_column='VesselAndDry', blank=True, null=True)  
    percent_water = models.FloatField(db_column='PercentWater', blank=True, null=True)  
    dry_tissue = models.FloatField(db_column='DryTissue', blank=True, null=True)  
    dry_tissue_type = models.CharField(db_column='DryTissueType', max_length=30, blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_freezedry'


class TblResultsMercury1(models.Model):
    r1id = models.AutoField(db_column='R1ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysis_date = models.DateField(db_column='AnalysisDate')  
    weight = models.FloatField(db_column='Weight')  
    height = models.FloatField(db_column='Height')  
    hg_ng = models.FloatField(db_column='Hg_ng')  
    dryc_ugkg = models.FloatField(db_column='DryC_ugkg')  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_mercury_1'


class TblResultsMercury2(models.Model):
    r2id = models.AutoField(db_column='R2ID', primary_key=True)  
    sample_test_id = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysis_date = models.DateField(db_column='AnalysisDate')  
    dry_log_id = models.CharField(db_column='DryLogID', max_length=15, blank=True, null=True)  
    aliquot_mass_g = models.FloatField(db_column='AliquotMass_g', blank=True, null=True)  
    hg_ugg_wet = models.FloatField(db_column='Hg_ugg_wet', blank=True, null=True)  
    batch = models.CharField(db_column='Batch', max_length=10, blank=True, null=True)  
    flag = models.TextField(db_column='Flag', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_mercury_2'


