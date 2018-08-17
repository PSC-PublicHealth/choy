# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TblTaxonomicId(models.Model):
    taxonomicid = models.CharField(db_column='TaxonomicID', primary_key=True, max_length=45)  
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  
    phylum = models.CharField(db_column='Phylum', max_length=20, blank=True, null=True)  
    subphylum = models.CharField(db_column='Subphylum', max_length=20, blank=True, null=True)  
    class_field = models.CharField(db_column='Class', max_length=20, blank=True, null=True)   
    order_field = models.CharField(db_column='Order_', max_length=20, blank=True, null=True)  
    family = models.CharField(db_column='Family', max_length=20, blank=True, null=True)  
    genus = models.CharField(db_column='Genus', max_length=20, blank=True, null=True)  
    species = models.CharField(db_column='Species', max_length=20, blank=True, null=True)  
    extra = models.CharField(db_column='Extra', max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_taxonomic_id'


class TblTrawlLog(models.Model):
    trawllogid = models.CharField(db_column='TrawlLogID', primary_key=True, max_length=20)  
    trawltype = models.CharField(db_column='TrawlType', max_length=45, blank=True, null=True)  
    netnumber = models.IntegerField(db_column='NetNumber', blank=True, null=True)  
    width_m = models.FloatField(db_column='Width_M', blank=True, null=True)  
    trawltime = models.DateField(db_column='TrawlTime', blank=True, null=True)  
    nightday = models.CharField(db_column='NightDay', max_length=1, blank=True, null=True)  
    lengthoftrawl_m = models.FloatField(db_column='LengthOfTrawl_M', blank=True, null=True)  
    timeopen = models.TimeField(db_column='TimeOpen', blank=True, null=True)  
    minimumdepth_m = models.FloatField(db_column='MinimumDepth_M', blank=True, null=True)  
    maximumdepth_m = models.FloatField(db_column='MaximumDepth_M', blank=True, null=True)  
    volumefiltered = models.FloatField(db_column='VolumeFiltered', blank=True, null=True)  
    start_deg_lat = models.DecimalField(db_column='Start_Deg_Lat', max_digits=2, decimal_places=0, blank=True, null=True)  
    start_mins_lat = models.DecimalField(db_column='Start_Mins_Lat', max_digits=10, decimal_places=8, blank=True, null=True)  
    start_deg_long = models.DecimalField(db_column='Start_Deg_Long', max_digits=2, decimal_places=0, blank=True, null=True)  
    start_mins_long = models.DecimalField(db_column='Start_Mins_Long', max_digits=10, decimal_places=8, blank=True, null=True)  
    end_deg_lat = models.DecimalField(db_column='End_Deg_Lat', max_digits=2, decimal_places=0, blank=True, null=True)  
    end_mins_lat = models.DecimalField(db_column='End_Mins_Lat', max_digits=10, decimal_places=8, blank=True, null=True)  
    end_deg_long = models.DecimalField(db_column='End_Deg_Long', max_digits=2, decimal_places=0, blank=True, null=True)  
    end_mins_long = models.DecimalField(db_column='End_Mins_Long', max_digits=10, decimal_places=8, blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_trawl_log'


class TblLab(models.Model):
    labid = models.IntegerField(db_column='LabID', primary_key=True)  
    labname = models.CharField(db_column='LabName', max_length=30)  
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  
    contactemail = models.CharField(db_column='ContactEmail', max_length=30, blank=True, null=True)  
    contactphone = models.CharField(db_column='ContactPhone', max_length=12, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_lab'


class TblSpecimenLog(models.Model):
    specimenlogid = models.IntegerField(db_column='SpecimenLogID', primary_key=True)  
    taxonomicid = models.ForeignKey('TblTaxonomicId', models.DO_NOTHING, db_column='TaxonomicID', blank=True, null=True)  
    length_mm = models.FloatField(db_column='Length_MM', blank=True, null=True)  
    length_type = models.CharField(db_column='Length_type', max_length=20, blank=True, null=True)  
    wet_whole_mass_g = models.FloatField(db_column='Wet_Whole_Mass_G', blank=True, null=True)  
    number_pooled_n = models.IntegerField(db_column='Number_Pooled_N', blank=True, null=True)  
    date_collected = models.DateField(db_column='Date_Collected', blank=True, null=True)  
    source = models.CharField(db_column='Source', max_length=45, blank=True, null=True)  
    trawllogid = models.ForeignKey('TblTrawlLog', models.DO_NOTHING, db_column='TrawlLogID', blank=True, null=True)  
    cruiselogid = models.IntegerField(db_column='CruiseLogID', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_specimen_log'


class TblSampleLog(models.Model):
    samplelogid = models.IntegerField(db_column='SampleLogID', primary_key=True)  
    acsampleid = models.CharField(db_column='ACSampleID', max_length=45, blank=True, null=True)  
    specimenlogid = models.ForeignKey('TblSpecimenLog', models.DO_NOTHING, db_column='SpecimenLogID')  
    tissuetype = models.CharField(db_column='TissueType', max_length=20, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_sample_log'


class TblSpecimenNoaa(models.Model):
    noaa_ll_specimenid = models.CharField(db_column='NOAA_LL_SpecimenID', primary_key=True, max_length=13)  
    specimenlogid = models.ForeignKey(TblSpecimenLog, models.DO_NOTHING, db_column='SpecimenLogID')  
    acsampleid = models.IntegerField(db_column='ACSampleID', blank=True, null=True)  
    triptype = models.CharField(db_column='TripType', max_length=1, blank=True, null=True)  
    time_tag = models.TimeField(db_column='Time_TAG', blank=True, null=True)  
    tripnumber = models.PositiveSmallIntegerField(db_column='TripNumber', blank=True, null=True)  
    bs_timestamp = models.DateTimeField(db_column='BS_TIMESTAMP')  
    bs_deg_lat = models.DecimalField(db_column='BS_DEG_LAT', max_digits=2, decimal_places=0, blank=True, null=True)  
    bs_min_lat = models.DecimalField(db_column='BS_MIN_LAT', max_digits=10, decimal_places=8, blank=True, null=True)  
    bs_deg_lon = models.DecimalField(db_column='BS_DEG_LON', max_digits=3, decimal_places=0, blank=True, null=True)  
    bs_min_lon = models.DecimalField(db_column='BS_MIN_LON', max_digits=10, decimal_places=8, blank=True, null=True)  
    be_timestamp = models.DateTimeField(db_column='BE_TIMESTAMP')  
    be_deg_lat = models.DecimalField(db_column='BE_DEG_LAT', max_digits=2, decimal_places=0, blank=True, null=True)  
    be_min_lat = models.DecimalField(db_column='BE_MIN_LAT', max_digits=10, decimal_places=8, blank=True, null=True)  
    be_deg_lon = models.DecimalField(db_column='BE_DEG_LON', max_digits=3, decimal_places=0, blank=True, null=True)  
    be_min_lon = models.DecimalField(db_column='BE_MIN_LON', max_digits=10, decimal_places=8, blank=True, null=True)  
    bh_timestamp = models.DateTimeField(db_column='BH_TIMESTAMP')  
    bh_deg_lat = models.DecimalField(db_column='BH_DEG_LAT', max_digits=2, decimal_places=0, blank=True, null=True)  
    bh_min_lat = models.DecimalField(db_column='BH_MIN_LAT', max_digits=10, decimal_places=8, blank=True, null=True)  
    bh_deg_lon = models.DecimalField(db_column='BH_DEG_LON', max_digits=3, decimal_places=0, blank=True, null=True)  
    bh_min_lon = models.DecimalField(db_column='BH_MIN_LON', max_digits=10, decimal_places=8, blank=True, null=True)  
    eh_deg_lat = models.DecimalField(db_column='EH_DEG_LAT', max_digits=2, decimal_places=0, blank=True, null=True)  
    eh_min_lat = models.DecimalField(db_column='EH_MIN_LAT', max_digits=10, decimal_places=8, blank=True, null=True)  
    eh_deg_lon = models.DecimalField(db_column='EH_DEG_LON', max_digits=3, decimal_places=0, blank=True, null=True)  
    eh_min_lon = models.DecimalField(db_column='EH_MIN_LON', max_digits=10, decimal_places=8, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_specimen_noaa'
        unique_together = (('noaa_ll_specimenid', 'specimenlogid'),)


class TblStmPredSumm(models.Model):
    predator_id = models.IntegerField(db_column='Predator_ID', primary_key=True)  
    predator_id_original = models.CharField(db_column='Predator_ID_Original', max_length=20, blank=True, null=True)  
    date_record = models.DateField(db_column='Date_Record', blank=True, null=True)  
    acsampleid = models.CharField(db_column='ACSampleID', max_length=45, blank=True, null=True)  
    weight_whole_g = models.FloatField(db_column='Weight_Whole_G', blank=True, null=True)  
    weight_cleaned_g = models.FloatField(db_column='Weight_Cleaned_G', blank=True, null=True)  
    bait_nb = models.IntegerField(db_column='Bait_NB', blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  
    fullness_coefficient = models.IntegerField(db_column='Fullness_Coefficient', blank=True, null=True)  
    samplelogid = models.ForeignKey(TblSampleLog, models.DO_NOTHING, db_column='SampleLogID', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_stm_pred_summ'


class TblStmPrey(models.Model):
    stm_preyid = models.IntegerField(db_column='Stm_PreyID', primary_key=True)  
    prey_taxonomicid = models.ForeignKey('TblTaxonomicId', models.DO_NOTHING, db_column='Prey_TaxonomicID', blank=True, null=True)  
    state_dvt = models.CharField(db_column='State_DVT', max_length=20, blank=True, null=True)  
    state_digestion = models.IntegerField(db_column='State_Digestion', blank=True, null=True)  
    nb_individuals = models.IntegerField(db_column='NB_Individuals', blank=True, null=True)  
    weight_tot = models.FloatField(db_column='Weight_Tot', blank=True, null=True)  
    comment_field = models.TextField(db_column='Comment_', blank=True, null=True)  
    preyitems_id_orig = models.CharField(db_column='PreyItems_ID_Orig', max_length=20, blank=True, null=True)  
    predator = models.ForeignKey(TblStmPredSumm, models.DO_NOTHING, db_column='Predator_ID', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_stm_prey'


class TblStmPreyIndividuals(models.Model):
    preyindividualsid = models.IntegerField(db_column='PreyIndividualsID', primary_key=True)  
    stm_preyid = models.ForeignKey(TblStmPrey, models.DO_NOTHING, db_column='Stm_PreyID', blank=True, null=True)  
    length_mm = models.FloatField(db_column='Length_MM', blank=True, null=True)  
    length_code = models.CharField(db_column='Length_Code', max_length=2, blank=True, null=True)  
    weight_g = models.FloatField(db_column='Weight_G', blank=True, null=True)  
    comment_field = models.TextField(db_column='Comment_', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'tbl_stm_prey_individuals'


class TblTests(models.Model):
    testid = models.IntegerField(db_column='TestID', primary_key=True)  
    testtype = models.CharField(db_column='TestType', max_length=20)  
    resulttable = models.CharField(db_column='ResultTable', max_length=20)  
    labid = models.ForeignKey(TblLab, models.DO_NOTHING, db_column='LabID')  

    class Meta:
        managed = True
        db_table = 'tbl_tests'


class TblSampleTests(models.Model):
    sampletestid = models.IntegerField(db_column='SampleTestID', primary_key=True)  
    sampleid = models.ForeignKey(TblSampleLog, models.DO_NOTHING, db_column='SampleID')  
    testid = models.ForeignKey('TblTests', models.DO_NOTHING, db_column='TestID')  
    resultid = models.IntegerField(db_column='ResultID', blank=True, null=True)  
    testsent = models.DateField(db_column='TestSent', blank=True, null=True)  
    resultrecd = models.DateField(db_column='ResultRecd', blank=True, null=True)  
    qaqc = models.IntegerField(db_column='QAQC')  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_sample_tests'


class TblResultsBulkStableIsotope(models.Model):
    r6id = models.IntegerField(db_column='R6ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    analyzedby = models.CharField(db_column='AnalyzedBy', max_length=30, blank=True, null=True)  
    hedilution = models.CharField(db_column='HeDilution', max_length=30, blank=True, null=True)  
    notes = models.TextField(db_column='Notes', blank=True, null=True)  
    weight_mg = models.FloatField(db_column='Weight_mg', blank=True, null=True)  
    n_ug = models.FloatField(db_column='N_ug', blank=True, null=True)  
    d15n = models.FloatField(db_column='d15N', blank=True, null=True)  
    c_ug = models.FloatField(db_column='C_ug', blank=True, null=True)  
    d13c = models.FloatField(db_column='d13C', blank=True, null=True)  
    acidified = models.IntegerField(db_column='Acidified')  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_bulk_stable_isotope'


class TblResultsCompSpecAaIsotope(models.Model):
    r5id = models.IntegerField(db_column='R5ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    runnum = models.CharField(db_column='RunNum', max_length=20)  
    aminoacid = models.CharField(db_column='AminoAcid', max_length=20, blank=True, null=True)  
    ea_irms = models.FloatField(db_column='EA-IRMS', blank=True, null=True) 
    rt = models.FloatField(db_column='RT', blank=True, null=True)  
    peak = models.IntegerField(db_column='Peak', blank=True, null=True)  
    rt2 = models.FloatField(db_column='RT2', blank=True, null=True)  
    area = models.FloatField(db_column='Area', blank=True, null=True)  
    d15n_un = models.FloatField(db_column='d15N_un', blank=True, null=True)  
    d15n_std = models.FloatField(db_column='d15N_std', blank=True, null=True)  
    d15n_reg = models.FloatField(db_column='d15N_reg', blank=True, null=True)  
    standard = models.CharField(db_column='Standard', max_length=30, blank=True, null=True)  
    vialid = models.CharField(db_column='VialID', max_length=20, blank=True, null=True)  
    sampleweight = models.FloatField(db_column='SampleWeight', blank=True, null=True)  
    ea_ul = models.IntegerField(db_column='EA_uL', blank=True, null=True)  
    injectionvolume = models.FloatField(db_column='InjectionVolume', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_comp_spec_AA_isotope'


class TblResultsFattyacid(models.Model):
    r4id = models.IntegerField(db_column='R4ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    csiro_id = models.TextField(db_column='CSIRO_ID')  
    noaa_ll_specimenid = models.TextField(db_column='NOAA_LL_SpecimenID')  
    tissuetype = models.CharField(db_column='TissueType', max_length=20, blank=True, null=True)  
    tissuelocation = models.CharField(db_column='TissueLocation', max_length=20, blank=True, null=True)  
    catchdate = models.DateField(db_column='CatchDate', blank=True, null=True)  
    forklength_cm = models.FloatField(db_column='Forklength_cm', blank=True, null=True)  
    wholemass_g = models.FloatField(db_column='WholeMass_g', blank=True, null=True)  
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  
    drymass_g = models.FloatField(db_column='DryMass_g', blank=True, null=True)  
    caplessvialandlipid_g = models.FloatField(db_column='CaplessVialAndLipid_g', blank=True, null=True)  
    caplessvial_g = models.FloatField(db_column='CaplessVial_g', blank=True, null=True)  
    lipidmass_g = models.FloatField(db_column='LipidMass_g', blank=True, null=True)  
    lipidmass_mg = models.FloatField(db_column='LipidMass_mg', blank=True, null=True)  
    c19_internal_standard_added_ul = models.IntegerField(db_column='C19_Internal_Standard_Added_ul', blank=True, null=True)  
    percentlipid_drywt = models.FloatField(db_column='PercentLipid_drywt', blank=True, null=True)  
    methylation_ul = models.IntegerField(db_column='Methylation_ul', blank=True, null=True)  
    tl_volume_ul = models.IntegerField(db_column='TL_Volume_ul', blank=True, null=True)  
    percentlipid_drywt_reweigh = models.FloatField(db_column='PercentLipid_drywt_reweigh', blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_fattyacid'


class TblResultsFreezedry(models.Model):
    r3id = models.IntegerField(db_column='R3ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    family = models.TextField(db_column='Family', blank=True, null=True)  
    genus = models.TextField(db_column='Genus', blank=True, null=True)  
    species = models.TextField(db_column='Species', blank=True, null=True)  
    counts = models.IntegerField(db_column='Counts', blank=True, null=True)  
    length1_type = models.CharField(db_column='Length1_type', max_length=20, blank=True, null=True)  
    length1_mm = models.IntegerField(db_column='Length1_mm', blank=True, null=True)  
    length2_type = models.CharField(db_column='Length2_type', max_length=20, blank=True, null=True)  
    length2_mm = models.IntegerField(db_column='Length2_mm', blank=True, null=True)  
    wholewetmass = models.IntegerField(db_column='WholeWetMass', blank=True, null=True)  
    wetremaining = models.TextField(db_column='WetRemaining', blank=True, null=True)  
    vessel = models.FloatField(db_column='Vessel', blank=True, null=True)  
    vesselandwet = models.FloatField(db_column='VesselAndWet', blank=True, null=True)  
    vesselanddry = models.FloatField(db_column='VesselAndDry', blank=True, null=True)  
    percentwater = models.FloatField(db_column='PercentWater', blank=True, null=True)  
    drytissue = models.FloatField(db_column='DryTissue', blank=True, null=True)  
    drytissuetype = models.CharField(db_column='DryTissueType', max_length=30, blank=True, null=True)  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_freezedry'


class TblResultsMercury1(models.Model):
    r1id = models.IntegerField(db_column='R1ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    weight = models.FloatField(db_column='Weight')  
    height = models.FloatField(db_column='Height')  
    hg_ng = models.FloatField(db_column='Hg_ng')  
    dryc_ugkg = models.FloatField(db_column='DryC_ugkg')  
    comments = models.TextField(db_column='Comments', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_mercury_1'


class TblResultsMercury2(models.Model):
    r2id = models.IntegerField(db_column='R2ID', primary_key=True)  
    sampletestid = models.ForeignKey('TblSampleTests', models.DO_NOTHING, db_column='SampleTestID')  
    analysisdate = models.DateField(db_column='AnalysisDate')  
    drylogid = models.CharField(db_column='DryLogID', max_length=15, blank=True, null=True)  
    aliquotmass_g = models.FloatField(db_column='AliquotMass_g', blank=True, null=True)  
    hg_ugg_wet = models.FloatField(db_column='Hg_ugg_wet', blank=True, null=True)  
    batch = models.CharField(db_column='Batch', max_length=10, blank=True, null=True)  
    flag = models.TextField(db_column='Flag', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'tbl_results_mercury_2'


