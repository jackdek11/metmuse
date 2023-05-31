from django.db import models


class Image(models.Model):
    ref = models.IntegerField(unique=True, primary_key=True)
    url = models.URLField()
    name = models.TextField(blank=True, null=True)
    artistDisplayName = models.TextField(blank=True, null=True)
    artistDisplayBio = models.TextField(blank=True, null=True)
    artistNationality = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)


class Blacklist(models.Model):
    ref = models.IntegerField(unique=True, primary_key=True)