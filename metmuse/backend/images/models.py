from django.db import models


class Image(models.Model):
    file = models.FileField(null=True)
    fetchable_image = models.OneToOneField('scheduling.FetchableImage', on_delete=models.CASCADE, primary_key=True)
    url = models.URLField()
    name = models.CharField(blank=True, max_length=180)
    artist_name = models.CharField(blank=True, max_length=180)
    artist_bio = models.CharField(blank=True, max_length=380)
    artist_nationality = models.CharField(blank=True, max_length=180)
    country = models.CharField(blank=True, max_length=180)
    region = models.CharField(blank=True, max_length=180)
    start_date = models.CharField(blank=True, max_length=4)
    end_date = models.CharField(blank=True, max_length=4)

    class Meta:
        db_table = 'metmuse.images'

    def __str__(self):
        return self.name or "No name found"

