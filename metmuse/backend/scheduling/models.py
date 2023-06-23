from django.db import models
from scheduling.enums import FetchStatus


class FetchableImages(models.Model):
    object_id = models.IntegerField()
    status = models.IntegerField(choices=FetchStatus.choices, default=FetchStatus.NEEDS_FETCHING)

    class Meta:
        db_table = 'metmuse.fetchable_images'
        verbose_name_plural = "Fetchable Images"

    def __str__(self):
        return self.object_id
