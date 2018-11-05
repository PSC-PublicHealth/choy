# Generated by Django 2.0.5 on 2018-11-05 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deepseaweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblOriginTypes',
            fields=[
                ('origintypeid', models.IntegerField(db_column='OriginID', primary_key=True, serialize=False)),
                ('originname', models.CharField(db_column='SubsampleType', max_length=20)),
            ],
            options={
                'db_table': 'tbl_origin_types',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='tblsample',
            name='in_stomach',
        ),
        migrations.RemoveField(
            model_name='tblsample',
            name='sample_origin',
        ),
        migrations.AddField(
            model_name='tblsample',
            name='originid',
            field=models.IntegerField(blank=True, db_column='SampleOriginID', default=0, null=True),
        ),
        migrations.AddField(
            model_name='tblsample',
            name='processingid',
            field=models.CharField(blank=True, db_column='ProcessingID', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tblsample',
            name='remaining_mass_g',
            field=models.FloatField(blank=True, db_column='Remaining_Mass_G', null=True),
        ),
        migrations.AddField(
            model_name='tblsample',
            name='origin_type',
            field=models.ForeignKey(db_column='OriginID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deepseaweb.TblOriginTypes'),
        ),
    ]