# Generated by Django 2.0.5 on 2018-08-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblLab',
            fields=[
                ('labid', models.IntegerField(db_column='LabID', primary_key=True, serialize=False)),
                ('labname', models.CharField(db_column='LabName', max_length=30)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('contactname', models.CharField(blank=True, db_column='ContactName', max_length=30, null=True)),
                ('contactemail', models.CharField(blank=True, db_column='ContactEmail', max_length=30, null=True)),
                ('contactphone', models.CharField(blank=True, db_column='ContactPhone', max_length=12, null=True)),
            ],
            options={
                'db_table': 'tbl_lab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsBulkStableIsotope',
            fields=[
                ('r6id', models.IntegerField(db_column='R6ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('analyzedby', models.CharField(blank=True, db_column='AnalyzedBy', max_length=30, null=True)),
                ('hedilution', models.CharField(blank=True, db_column='HeDilution', max_length=30, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('weight_mg', models.FloatField(blank=True, db_column='Weight_mg', null=True)),
                ('n_ug', models.FloatField(blank=True, db_column='N_ug', null=True)),
                ('d15n', models.FloatField(blank=True, db_column='d15N', null=True)),
                ('c_ug', models.FloatField(blank=True, db_column='C_ug', null=True)),
                ('d13c', models.FloatField(blank=True, db_column='d13C', null=True)),
                ('acidified', models.IntegerField(db_column='Acidified')),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tbl_results_bulk_stable_isotope',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsCompSpecAaIsotope',
            fields=[
                ('r5id', models.IntegerField(db_column='R5ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('runnum', models.CharField(db_column='RunNum', max_length=20)),
                ('aminoacid', models.CharField(blank=True, db_column='AminoAcid', max_length=20, null=True)),
                ('ea_irms', models.FloatField(blank=True, db_column='EA-IRMS', null=True)),
                ('rt', models.FloatField(blank=True, db_column='RT', null=True)),
                ('peak', models.IntegerField(blank=True, db_column='Peak', null=True)),
                ('rt2', models.FloatField(blank=True, db_column='RT2', null=True)),
                ('area', models.FloatField(blank=True, db_column='Area', null=True)),
                ('d15n_un', models.FloatField(blank=True, db_column='d15N_un', null=True)),
                ('d15n_std', models.FloatField(blank=True, db_column='d15N_std', null=True)),
                ('d15n_reg', models.FloatField(blank=True, db_column='d15N_reg', null=True)),
                ('standard', models.CharField(blank=True, db_column='Standard', max_length=30, null=True)),
                ('vialid', models.CharField(blank=True, db_column='VialID', max_length=20, null=True)),
                ('sampleweight', models.FloatField(blank=True, db_column='SampleWeight', null=True)),
                ('ea_ul', models.IntegerField(blank=True, db_column='EA_uL', null=True)),
                ('injectionvolume', models.FloatField(blank=True, db_column='InjectionVolume', null=True)),
            ],
            options={
                'db_table': 'tbl_results_comp_spec_AA_isotope',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsFattyacid',
            fields=[
                ('r4id', models.IntegerField(db_column='R4ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('csiro_id', models.TextField(db_column='CSIRO_ID')),
                ('noaa_ll_specimenid', models.TextField(db_column='NOAA_LL_SpecimenID')),
                ('tissuetype', models.CharField(blank=True, db_column='TissueType', max_length=20, null=True)),
                ('tissuelocation', models.CharField(blank=True, db_column='TissueLocation', max_length=20, null=True)),
                ('catchdate', models.DateField(blank=True, db_column='CatchDate', null=True)),
                ('forklength_cm', models.FloatField(blank=True, db_column='Forklength_cm', null=True)),
                ('wholemass_g', models.FloatField(blank=True, db_column='WholeMass_g', null=True)),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=1, null=True)),
                ('drymass_g', models.FloatField(blank=True, db_column='DryMass_g', null=True)),
                ('caplessvialandlipid_g', models.FloatField(blank=True, db_column='CaplessVialAndLipid_g', null=True)),
                ('caplessvial_g', models.FloatField(blank=True, db_column='CaplessVial_g', null=True)),
                ('lipidmass_g', models.FloatField(blank=True, db_column='LipidMass_g', null=True)),
                ('lipidmass_mg', models.FloatField(blank=True, db_column='LipidMass_mg', null=True)),
                ('c19_internal_standard_added_ul', models.IntegerField(blank=True, db_column='C19_Internal_Standard_Added_ul', null=True)),
                ('percentlipid_drywt', models.FloatField(blank=True, db_column='PercentLipid_drywt', null=True)),
                ('methylation_ul', models.IntegerField(blank=True, db_column='Methylation_ul', null=True)),
                ('tl_volume_ul', models.IntegerField(blank=True, db_column='TL_Volume_ul', null=True)),
                ('percentlipid_drywt_reweigh', models.FloatField(blank=True, db_column='PercentLipid_drywt_reweigh', null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tbl_results_fattyacid',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsFreezedry',
            fields=[
                ('r3id', models.IntegerField(db_column='R3ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('family', models.TextField(blank=True, db_column='Family', null=True)),
                ('genus', models.TextField(blank=True, db_column='Genus', null=True)),
                ('species', models.TextField(blank=True, db_column='Species', null=True)),
                ('counts', models.IntegerField(blank=True, db_column='Counts', null=True)),
                ('length1_type', models.CharField(blank=True, db_column='Length1_type', max_length=20, null=True)),
                ('length1_mm', models.IntegerField(blank=True, db_column='Length1_mm', null=True)),
                ('length2_type', models.CharField(blank=True, db_column='Length2_type', max_length=20, null=True)),
                ('length2_mm', models.IntegerField(blank=True, db_column='Length2_mm', null=True)),
                ('wholewetmass', models.IntegerField(blank=True, db_column='WholeWetMass', null=True)),
                ('wetremaining', models.TextField(blank=True, db_column='WetRemaining', null=True)),
                ('vessel', models.FloatField(blank=True, db_column='Vessel', null=True)),
                ('vesselandwet', models.FloatField(blank=True, db_column='VesselAndWet', null=True)),
                ('vesselanddry', models.FloatField(blank=True, db_column='VesselAndDry', null=True)),
                ('percentwater', models.FloatField(blank=True, db_column='PercentWater', null=True)),
                ('drytissue', models.FloatField(blank=True, db_column='DryTissue', null=True)),
                ('drytissuetype', models.CharField(blank=True, db_column='DryTissueType', max_length=30, null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tbl_results_freezedry',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsMercury1',
            fields=[
                ('r1id', models.IntegerField(db_column='R1ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('weight', models.FloatField(db_column='Weight')),
                ('height', models.FloatField(db_column='Height')),
                ('hg_ng', models.FloatField(db_column='Hg_ng')),
                ('dryc_ugkg', models.FloatField(db_column='DryC_ugkg')),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tbl_results_mercury_1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblResultsMercury2',
            fields=[
                ('r2id', models.IntegerField(db_column='R2ID', primary_key=True, serialize=False)),
                ('analysisdate', models.DateField(db_column='AnalysisDate')),
                ('drylogid', models.CharField(blank=True, db_column='DryLogID', max_length=15, null=True)),
                ('aliquotmass_g', models.FloatField(blank=True, db_column='AliquotMass_g', null=True)),
                ('hg_ugg_wet', models.FloatField(blank=True, db_column='Hg_ugg_wet', null=True)),
                ('batch', models.CharField(blank=True, db_column='Batch', max_length=10, null=True)),
                ('flag', models.TextField(blank=True, db_column='Flag', null=True)),
            ],
            options={
                'db_table': 'tbl_results_mercury_2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblSampleLog',
            fields=[
                ('samplelogid', models.IntegerField(db_column='SampleLogID', primary_key=True, serialize=False)),
                ('acsampleid', models.CharField(blank=True, db_column='ACSampleID', max_length=45, null=True)),
                ('tissuetype', models.CharField(blank=True, db_column='TissueType', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_sample_log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblSampleTests',
            fields=[
                ('sampletestid', models.IntegerField(db_column='SampleTestID', primary_key=True, serialize=False)),
                ('resultid', models.IntegerField(blank=True, db_column='ResultID', null=True)),
                ('testsent', models.DateField(blank=True, db_column='TestSent', null=True)),
                ('resultrecd', models.DateField(blank=True, db_column='ResultRecd', null=True)),
                ('qaqc', models.IntegerField(db_column='QAQC')),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
                ('sampleid', models.ForeignKey(db_column='SampleID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleLog')),
            ],
            options={
                'db_table': 'tbl_sample_tests',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblSpecimenLog',
            fields=[
                ('specimenlogid', models.IntegerField(db_column='SpecimenLogID', primary_key=True, serialize=False)),
                ('length_mm', models.FloatField(blank=True, db_column='Length_MM', null=True)),
                ('length_type', models.CharField(blank=True, db_column='Length_type', max_length=20, null=True)),
                ('wet_whole_mass_g', models.FloatField(blank=True, db_column='Wet_Whole_Mass_G', null=True)),
                ('number_pooled_n', models.IntegerField(blank=True, db_column='Number_Pooled_N', null=True)),
                ('date_collected', models.DateField(blank=True, db_column='Date_Collected', null=True)),
                ('source', models.CharField(blank=True, db_column='Source', max_length=45, null=True)),
                ('cruiselogid', models.IntegerField(blank=True, db_column='CruiseLogID', null=True)),
            ],
            options={
                'db_table': 'tbl_specimen_log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblSpecimenNoaa',
            fields=[
                ('noaa_ll_specimenid', models.CharField(db_column='NOAA_LL_SpecimenID', max_length=13, primary_key=True, serialize=False)),
                ('acsampleid', models.IntegerField(blank=True, db_column='ACSampleID', null=True)),
                ('triptype', models.CharField(blank=True, db_column='TripType', max_length=1, null=True)),
                ('time_tag', models.TimeField(blank=True, db_column='Time_TAG', null=True)),
                ('tripnumber', models.PositiveSmallIntegerField(blank=True, db_column='TripNumber', null=True)),
                ('bs_timestamp', models.DateTimeField(db_column='BS_TIMESTAMP')),
                ('bs_deg_lat', models.DecimalField(blank=True, db_column='BS_DEG_LAT', decimal_places=0, max_digits=2, null=True)),
                ('bs_min_lat', models.DecimalField(blank=True, db_column='BS_MIN_LAT', decimal_places=8, max_digits=10, null=True)),
                ('bs_deg_lon', models.DecimalField(blank=True, db_column='BS_DEG_LON', decimal_places=0, max_digits=3, null=True)),
                ('bs_min_lon', models.DecimalField(blank=True, db_column='BS_MIN_LON', decimal_places=8, max_digits=10, null=True)),
                ('be_timestamp', models.DateTimeField(db_column='BE_TIMESTAMP')),
                ('be_deg_lat', models.DecimalField(blank=True, db_column='BE_DEG_LAT', decimal_places=0, max_digits=2, null=True)),
                ('be_min_lat', models.DecimalField(blank=True, db_column='BE_MIN_LAT', decimal_places=8, max_digits=10, null=True)),
                ('be_deg_lon', models.DecimalField(blank=True, db_column='BE_DEG_LON', decimal_places=0, max_digits=3, null=True)),
                ('be_min_lon', models.DecimalField(blank=True, db_column='BE_MIN_LON', decimal_places=8, max_digits=10, null=True)),
                ('bh_timestamp', models.DateTimeField(db_column='BH_TIMESTAMP')),
                ('bh_deg_lat', models.DecimalField(blank=True, db_column='BH_DEG_LAT', decimal_places=0, max_digits=2, null=True)),
                ('bh_min_lat', models.DecimalField(blank=True, db_column='BH_MIN_LAT', decimal_places=8, max_digits=10, null=True)),
                ('bh_deg_lon', models.DecimalField(blank=True, db_column='BH_DEG_LON', decimal_places=0, max_digits=3, null=True)),
                ('bh_min_lon', models.DecimalField(blank=True, db_column='BH_MIN_LON', decimal_places=8, max_digits=10, null=True)),
                ('eh_deg_lat', models.DecimalField(blank=True, db_column='EH_DEG_LAT', decimal_places=0, max_digits=2, null=True)),
                ('eh_min_lat', models.DecimalField(blank=True, db_column='EH_MIN_LAT', decimal_places=8, max_digits=10, null=True)),
                ('eh_deg_lon', models.DecimalField(blank=True, db_column='EH_DEG_LON', decimal_places=0, max_digits=3, null=True)),
                ('eh_min_lon', models.DecimalField(blank=True, db_column='EH_MIN_LON', decimal_places=8, max_digits=10, null=True)),
                ('specimenlogid', models.ForeignKey(db_column='SpecimenLogID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSpecimenLog')),
            ],
            options={
                'db_table': 'tbl_specimen_noaa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblStmPredSumm',
            fields=[
                ('predator_id', models.IntegerField(db_column='Predator_ID', primary_key=True, serialize=False)),
                ('predator_id_original', models.CharField(blank=True, db_column='Predator_ID_Original', max_length=20, null=True)),
                ('date_record', models.DateField(blank=True, db_column='Date_Record', null=True)),
                ('acsampleid', models.CharField(blank=True, db_column='ACSampleID', max_length=45, null=True)),
                ('weight_whole_g', models.FloatField(blank=True, db_column='Weight_Whole_G', null=True)),
                ('weight_cleaned_g', models.FloatField(blank=True, db_column='Weight_Cleaned_G', null=True)),
                ('bait_nb', models.IntegerField(blank=True, db_column='Bait_NB', null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
                ('fullness_coefficient', models.IntegerField(blank=True, db_column='Fullness_Coefficient', null=True)),
                ('samplelogid', models.ForeignKey(blank=True, db_column='SampleLogID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleLog')),
            ],
            options={
                'db_table': 'tbl_stm_pred_summ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblStmPrey',
            fields=[
                ('stm_preyid', models.IntegerField(db_column='Stm_PreyID', primary_key=True, serialize=False)),
                ('state_dvt', models.CharField(blank=True, db_column='State_DVT', max_length=20, null=True)),
                ('state_digestion', models.IntegerField(blank=True, db_column='State_Digestion', null=True)),
                ('nb_individuals', models.IntegerField(blank=True, db_column='NB_Individuals', null=True)),
                ('weight_tot', models.FloatField(blank=True, db_column='Weight_Tot', null=True)),
                ('comment_field', models.TextField(blank=True, db_column='Comment_', null=True)),
                ('preyitems_id_orig', models.CharField(blank=True, db_column='PreyItems_ID_Orig', max_length=20, null=True)),
                ('predator', models.ForeignKey(blank=True, db_column='Predator_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblStmPredSumm')),
            ],
            options={
                'db_table': 'tbl_stm_prey',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblStmPreyIndividuals',
            fields=[
                ('preyindividualsid', models.IntegerField(db_column='PreyIndividualsID', primary_key=True, serialize=False)),
                ('length_mm', models.FloatField(blank=True, db_column='Length_MM', null=True)),
                ('length_code', models.CharField(blank=True, db_column='Length_Code', max_length=2, null=True)),
                ('weight_g', models.FloatField(blank=True, db_column='Weight_G', null=True)),
                ('comment_field', models.TextField(blank=True, db_column='Comment_', null=True)),
                ('stm_preyid', models.ForeignKey(blank=True, db_column='Stm_PreyID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblStmPrey')),
            ],
            options={
                'db_table': 'tbl_stm_prey_individuals',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblTaxonomicId',
            fields=[
                ('taxonomicid', models.CharField(db_column='TaxonomicID', max_length=45, primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=20, null=True)),
                ('phylum', models.CharField(blank=True, db_column='Phylum', max_length=20, null=True)),
                ('subphylum', models.CharField(blank=True, db_column='Subphylum', max_length=20, null=True)),
                ('class_field', models.CharField(blank=True, db_column='Class', max_length=20, null=True)),
                ('order_field', models.CharField(blank=True, db_column='Order_', max_length=20, null=True)),
                ('family', models.CharField(blank=True, db_column='Family', max_length=20, null=True)),
                ('genus', models.CharField(blank=True, db_column='Genus', max_length=20, null=True)),
                ('species', models.CharField(blank=True, db_column='Species', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_taxonomic_id',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblTests',
            fields=[
                ('testid', models.IntegerField(db_column='TestID', primary_key=True, serialize=False)),
                ('testtype', models.CharField(db_column='TestType', max_length=20)),
                ('resulttable', models.CharField(db_column='ResultTable', max_length=20)),
                ('labid', models.ForeignKey(db_column='LabID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblLab')),
            ],
            options={
                'db_table': 'tbl_tests',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblTrawlLog',
            fields=[
                ('trawllogid', models.CharField(db_column='TrawlLogID', max_length=20, primary_key=True, serialize=False)),
                ('trawltype', models.CharField(blank=True, db_column='TrawlType', max_length=45, null=True)),
                ('netnumber', models.IntegerField(blank=True, db_column='NetNumber', null=True)),
                ('width_m', models.FloatField(blank=True, db_column='Width_M', null=True)),
                ('trawltime', models.DateField(blank=True, db_column='TrawlTime', null=True)),
                ('nightday', models.CharField(blank=True, db_column='NightDay', max_length=1, null=True)),
                ('lengthoftrawl_m', models.FloatField(blank=True, db_column='LengthOfTrawl_M', null=True)),
                ('timeopen', models.TimeField(blank=True, db_column='TimeOpen', null=True)),
                ('minimumdepth_m', models.FloatField(blank=True, db_column='MinimumDepth_M', null=True)),
                ('maximumdepth_m', models.FloatField(blank=True, db_column='MaximumDepth_M', null=True)),
                ('volumefiltered', models.FloatField(blank=True, db_column='VolumeFiltered', null=True)),
                ('start_deg_lat', models.DecimalField(blank=True, db_column='Start_Deg_Lat', decimal_places=0, max_digits=2, null=True)),
                ('start_mins_lat', models.DecimalField(blank=True, db_column='Start_Mins_Lat', decimal_places=8, max_digits=10, null=True)),
                ('start_deg_long', models.DecimalField(blank=True, db_column='Start_Deg_Long', decimal_places=0, max_digits=2, null=True)),
                ('start_mins_long', models.DecimalField(blank=True, db_column='Start_Mins_Long', decimal_places=8, max_digits=10, null=True)),
                ('end_deg_lat', models.DecimalField(blank=True, db_column='End_Deg_Lat', decimal_places=0, max_digits=2, null=True)),
                ('end_mins_lat', models.DecimalField(blank=True, db_column='End_Mins_Lat', decimal_places=8, max_digits=10, null=True)),
                ('end_deg_long', models.DecimalField(blank=True, db_column='End_Deg_Long', decimal_places=0, max_digits=2, null=True)),
                ('end_mins_long', models.DecimalField(blank=True, db_column='End_Mins_Long', decimal_places=8, max_digits=10, null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tbl_trawl_log',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tblstmprey',
            name='prey_taxonomicid',
            field=models.ForeignKey(blank=True, db_column='Prey_TaxonomicID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblTaxonomicId'),
        ),
        migrations.AddField(
            model_name='tblspecimenlog',
            name='taxonomicid',
            field=models.ForeignKey(blank=True, db_column='TaxonomicID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblTaxonomicId'),
        ),
        migrations.AddField(
            model_name='tblspecimenlog',
            name='trawllogid',
            field=models.ForeignKey(blank=True, db_column='TrawlLogID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblTrawlLog'),
        ),
        migrations.AddField(
            model_name='tblsampletests',
            name='testid',
            field=models.ForeignKey(db_column='TestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblTests'),
        ),
        migrations.AddField(
            model_name='tblsamplelog',
            name='specimenlogid',
            field=models.ForeignKey(db_column='SpecimenLogID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSpecimenLog'),
        ),
        migrations.AddField(
            model_name='tblresultsmercury2',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AddField(
            model_name='tblresultsmercury1',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AddField(
            model_name='tblresultsfreezedry',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AddField(
            model_name='tblresultsfattyacid',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AddField(
            model_name='tblresultscompspecaaisotope',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AddField(
            model_name='tblresultsbulkstableisotope',
            name='sampletestid',
            field=models.ForeignKey(db_column='SampleTestID', on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblSampleTests'),
        ),
        migrations.AlterUniqueTogether(
            name='tblspecimennoaa',
            unique_together={('noaa_ll_specimenid', 'specimenlogid')},
        ),
    ]