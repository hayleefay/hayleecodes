from django.db import models

class Bilateral(models.Model):
    region_orig = models.CharField(max_length=200)
    region_orig_id = models.IntegerField(default=0)
    region_dest = models.CharField(max_length=200)
    region_dest_id = models.IntegerField(default=0)
    country_orig = models.CharField(max_length=200)
    country_orig_id = models.CharField(max_length=200)
    country_dest = models.CharField(max_length=200)
    country_dest_id = models.CharField(max_length=200)
    regionflow_1990 = models.IntegerField(default=0)
    regionflow_1995 = models.IntegerField(default=0)
    regionflow_2000 = models.IntegerField(default=0)
    regionflow_2005 = models.IntegerField(default=0)
    countryflow_1990 = models.IntegerField(default=0)
    countryflow_1995 = models.IntegerField(default=0)
    countryflow_2000 = models.IntegerField(default=0)
    countryflow_2005 = models.IntegerField(default=0)
    metadata = models.CharField(max_length=200)
