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
    description = models.CharField(max_length=500)
    who = models.CharField(max_length=100)
    sourcetype = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    oppt_phase = models.IntegerField()
    processed = models.IntegerField()
    harm_init = models.IntegerField()
    harm_mapped = models.IntegerField()
    loaded = models.IntegerField()
    icfsource = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
