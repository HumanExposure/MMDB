# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    """
    Provides metadata for all other models
    created_at
    modified_at
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Source(BaseModel):
    description = models.CharField(max_length=500, null=True)
    who = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=45, null=True)
    name = models.CharField(max_length=45, null=True)
    oppt_phase = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    harm_init = models.BooleanField(default=False)
    harm_mapped = models.BooleanField(default=False)
    loaded = models.BooleanField(default=False)
    full_source_name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)


class Media(BaseModel):
    reported_media = models.CharField(max_length=200, null=True)
    harmonized_medium = models.CharField(max_length=200, null=True)
    reported_species = models.CharField(max_length=200, null=True)
    source = models.ForeignKey(Source, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.reported_media


class Substances(BaseModel):
    reported_casrn = models.CharField(max_length=30, null=True)
    reported_chemical_name = models.CharField(max_length=400, null=True)
    dtxsid = models.CharField(max_length=20, null=True)
    preferred_name = models.CharField(max_length=300, null=True)
    casrn = models.CharField(max_length=20, null=True)
    date_modified = models.TextField(null=True)
    date_uploaded = models.TextField(null=True)
    howcurated = models.TextField(null=True)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    dtxrid = models.CharField(max_length=20, null=True)
    external_id = models.TextField(null=True)
    substance_type = models.TextField(null=True)
    structure_inchikey = models.TextField(null=True)
    structure_formula = models.TextField(null=True)

    def __str__(self):
        return self.reported_casrn


class Files(BaseModel):
    location = models.CharField(max_length=45, null=True)
    filename = models.CharField(max_length=200, null=True)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    n_records = models.IntegerField(null=True)
    mapped = models.BooleanField(default=False)
    harm_init = models.BooleanField(default=False)
    raw_init = models.BooleanField(null=True)

    def __str__(self):
        return self.filename


class HarmonizedRaw(BaseModel):
    reported_collection_activity_id = models.CharField(max_length=100, null=True)
    reported_sample_id = models.CharField(max_length=100, null=True)
    substance_id = models.CharField(max_length=200, null=True)
    reported_chemical_name = models.CharField(max_length=400, null=True)
    reported_casrn = models.CharField(max_length=20, null=True)
    reported_species = models.CharField(max_length=200, null=True)
    reported_media = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=100, null=True)
    us_state = models.CharField(max_length=45, null=True)
    us_county = models.CharField(max_length=60, null=True)
    reported_location = models.CharField(max_length=250, null=True)
    reported_date = models.CharField(max_length=45, null=True)
    reported_result = models.CharField(max_length=100, null=True)
    concentration = models.CharField(max_length=45, null=True)
    reported_units = models.CharField(max_length=100, null=True)
    loq = models.CharField(max_length=45, null=True)
    lod = models.CharField(max_length=45, null=True)
    other_limit = models.CharField(max_length=45, null=True)
    sample_year = models.CharField(max_length=4, null=True)
    sample_month = models.CharField(max_length=4, null=True)
    other_limit_description = models.CharField(max_length=150, null=True)
    nd_flag = models.CharField(max_length=100, null=True)
    qc_flag = models.CharField(max_length=100, null=True)
    reported_reference = models.CharField(max_length=300, null=True)
    detect_flag = models.CharField(max_length=45, null=True)
    record_id = models.IntegerField()
    files = models.ForeignKey(Files, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    reported_analytical_method = models.CharField(max_length=1000, null=True)
    result_flag = models.CharField(max_length=500, null=True)
    reported_link = models.CharField(max_length=500, null=True)
    detected = models.BooleanField(null=True)
    substances = models.ForeignKey(Substances, on_delete=models.PROTECT, null=True)
    media = models.ForeignKey(Media, on_delete=models.PROTECT)
    detect_conflict = models.BooleanField(null=True)

    def __str__(self):
        return self.reported_chemical_name

    class Meta:
        unique_together = [
            ("files", "source", "record_id"),
        ]


class HarmonizedAggregate(BaseModel):
    record_id = models.IntegerField()
    reported_data_id = models.CharField(max_length=45, null=True)
    reported_species = models.CharField(max_length=200, null=True)
    reported_media = models.CharField(max_length=120, null=True)
    country = models.CharField(max_length=45, null=True)
    us_state = models.CharField(max_length=45, null=True)
    reported_dates = models.CharField(max_length=45, null=True)
    years = models.CharField(max_length=45, null=True)
    reported_units = models.CharField(max_length=100, null=True)
    loq = models.CharField(max_length=45, null=True)
    lod = models.CharField(max_length=45, null=True)
    reported_n = models.CharField(max_length=45, null=True)
    reported_num_detects = models.CharField(max_length=45, null=True)
    reported_detect_rate = models.CharField(max_length=45, null=True)
    reported_reference = models.CharField(max_length=300, null=True)
    other_limit = models.CharField(max_length=45, null=True)
    other_limit_description = models.CharField(max_length=45, null=True)
    reported_population = models.CharField(max_length=500, null=True)
    reported_chemical_name = models.CharField(max_length=200, null=True)
    reported_casrn = models.CharField(max_length=50, null=True)
    files = models.ForeignKey(Files, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    reported_location = models.CharField(max_length=500, null=True)
    reported_project_id = models.CharField(max_length=45, null=True)
    reported_link = models.CharField(max_length=500, null=True)
    reported_num_nds = models.CharField(max_length=45, null=True)
    reported_collection_activity_id = models.CharField(max_length=100, null=True)
    reported_statistic = models.CharField(max_length=100, null=True)
    reported_result = models.CharField(max_length=45, null=True)
    reported_ages = models.CharField(max_length=45, null=True)
    reported_gender = models.CharField(max_length=45, null=True)
    reported_nondetect_rate = models.CharField(max_length=45, null=True)
    reported_race = models.CharField(max_length=45, null=True)
    reported_subpopulation = models.CharField(max_length=45, null=True)
    detected = models.BooleanField(null=True)
    substances = models.ForeignKey(Substances, on_delete=models.PROTECT, null=True)
    media = models.ForeignKey(Media, on_delete=models.PROTECT)
    qc_flag = models.CharField(max_length=200, null=True)
    us_county = models.CharField(max_length=60, null=True)
    detect_conflict = models.BooleanField(null=True)

    def __str__(self):
        return self.reported_chemical_name

    class Meta:
        unique_together = [
            ("files", "source", "record_id"),
        ]
