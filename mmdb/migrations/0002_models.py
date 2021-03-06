# Generated by Django 3.1.4 on 2021-01-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='icfsource',
        ),
        migrations.RemoveField(
            model_name='source',
            name='sourcetype',
        ),
        migrations.AddField(
            model_name='source',
            name='full_source_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='type',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='harm_init',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='source',
            name='harm_mapped',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='source',
            name='loaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='oppt_phase',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='source',
            name='who',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Substances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('reported_casrn', models.CharField(max_length=30, null=True)),
                ('reported_chemical_name', models.CharField(max_length=400, null=True)),
                ('dtxsid', models.CharField(max_length=20, null=True)),
                ('preferred_name', models.CharField(max_length=300, null=True)),
                ('casrn', models.CharField(max_length=20, null=True)),
                ('date_modified', models.TextField(null=True)),
                ('date_uploaded', models.TextField(null=True)),
                ('howcurated', models.TextField(null=True)),
                ('dtxrid', models.CharField(max_length=20, null=True)),
                ('external_id', models.TextField(null=True)),
                ('substance_type', models.TextField(null=True)),
                ('structure_inchikey', models.TextField(null=True)),
                ('structure_formula', models.TextField(null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.source')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('reported_media', models.CharField(max_length=200, null=True)),
                ('harmonized_medium', models.CharField(max_length=200, null=True)),
                ('reported_species', models.CharField(max_length=200, null=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mmdb.source')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=45, null=True)),
                ('filename', models.CharField(max_length=200, null=True)),
                ('n_records', models.IntegerField(null=True)),
                ('mapped', models.BooleanField(default=False)),
                ('harm_init', models.BooleanField(default=False)),
                ('raw_init', models.BooleanField(null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.source')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HarmonizedRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('reported_collection_activity_id', models.CharField(max_length=100, null=True)),
                ('reported_sample_id', models.CharField(max_length=100, null=True)),
                ('substance_id', models.CharField(max_length=200, null=True)),
                ('reported_chemical_name', models.CharField(max_length=400, null=True)),
                ('reported_casrn', models.CharField(max_length=20, null=True)),
                ('reported_species', models.CharField(max_length=200, null=True)),
                ('reported_media', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('us_state', models.CharField(max_length=45, null=True)),
                ('us_county', models.CharField(max_length=60, null=True)),
                ('reported_location', models.CharField(max_length=250, null=True)),
                ('reported_date', models.CharField(max_length=45, null=True)),
                ('reported_result', models.CharField(max_length=100, null=True)),
                ('concentration', models.CharField(max_length=45, null=True)),
                ('reported_units', models.CharField(max_length=100, null=True)),
                ('loq', models.CharField(max_length=45, null=True)),
                ('lod', models.CharField(max_length=45, null=True)),
                ('other_limit', models.CharField(max_length=45, null=True)),
                ('sample_year', models.CharField(max_length=4, null=True)),
                ('sample_month', models.CharField(max_length=4, null=True)),
                ('other_limit_description', models.CharField(max_length=150, null=True)),
                ('nd_flag', models.CharField(max_length=100, null=True)),
                ('qc_flag', models.CharField(max_length=100, null=True)),
                ('reported_reference', models.CharField(max_length=300, null=True)),
                ('detect_flag', models.CharField(max_length=45, null=True)),
                ('record_id', models.IntegerField()),
                ('reported_analytical_method', models.CharField(max_length=1000, null=True)),
                ('result_flag', models.CharField(max_length=500, null=True)),
                ('reported_link', models.CharField(max_length=500, null=True)),
                ('detected', models.BooleanField(null=True)),
                ('detect_conflict', models.BooleanField(null=True)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.files')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.media')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.source')),
                ('substances', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mmdb.substances')),
            ],
            options={
                'unique_together': {('files', 'source', 'record_id')},
            },
        ),
        migrations.CreateModel(
            name='HarmonizedAggregate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('record_id', models.IntegerField()),
                ('reported_data_id', models.CharField(max_length=45, null=True)),
                ('reported_species', models.CharField(max_length=200, null=True)),
                ('reported_media', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=45, null=True)),
                ('us_state', models.CharField(max_length=45, null=True)),
                ('reported_dates', models.CharField(max_length=45, null=True)),
                ('years', models.CharField(max_length=45, null=True)),
                ('reported_units', models.CharField(max_length=100, null=True)),
                ('loq', models.CharField(max_length=45, null=True)),
                ('lod', models.CharField(max_length=45, null=True)),
                ('reported_n', models.CharField(max_length=45, null=True)),
                ('reported_num_detects', models.CharField(max_length=45, null=True)),
                ('reported_detect_rate', models.CharField(max_length=45, null=True)),
                ('reported_reference', models.CharField(max_length=300, null=True)),
                ('other_limit', models.CharField(max_length=45, null=True)),
                ('other_limit_description', models.CharField(max_length=45, null=True)),
                ('reported_population', models.CharField(max_length=500, null=True)),
                ('reported_chemical_name', models.CharField(max_length=200, null=True)),
                ('reported_casrn', models.CharField(max_length=50, null=True)),
                ('reported_location', models.CharField(max_length=500, null=True)),
                ('reported_project_id', models.CharField(max_length=45, null=True)),
                ('reported_link', models.CharField(max_length=500, null=True)),
                ('reported_num_nds', models.CharField(max_length=45, null=True)),
                ('reported_collection_activity_id', models.CharField(max_length=100, null=True)),
                ('reported_statistic', models.CharField(max_length=100, null=True)),
                ('reported_result', models.CharField(max_length=45, null=True)),
                ('reported_ages', models.CharField(max_length=45, null=True)),
                ('reported_gender', models.CharField(max_length=45, null=True)),
                ('reported_nondetect_rate', models.CharField(max_length=45, null=True)),
                ('reported_race', models.CharField(max_length=45, null=True)),
                ('reported_subpopulation', models.CharField(max_length=45, null=True)),
                ('detected', models.BooleanField(null=True)),
                ('qc_flag', models.CharField(max_length=200, null=True)),
                ('us_county', models.CharField(max_length=60, null=True)),
                ('detect_conflict', models.BooleanField(null=True)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.files')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.media')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mmdb.source')),
                ('substances', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mmdb.substances')),
            ],
            options={
                'unique_together': {('files', 'source', 'record_id')},
            },
        ),
    ]
