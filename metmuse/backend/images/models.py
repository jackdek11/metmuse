from django.db import models


class Image(models.Model):
    file = models.FileField(null=True)
    fetchable_image = models.OneToOneField('scheduling.FetchableImages', on_delete=models.CASCADE, primary_key=True)
    url = models.URLField()
    name = models.TextField(blank=True, null=True)
    artistDisplayName = models.TextField(blank=True, null=True)
    artistDisplayBio = models.TextField(blank=True, null=True)
    artistNationality = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'metmuse.images'

    def __str__(self):
        return str(self.name) or "No name found"

