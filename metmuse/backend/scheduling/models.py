from django.db import models
from scheduling.enums import FetchStatus


class Department(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        db_table = 'metmuse.departments'

    def __str__(self):
        return self.name


class FetchableImages(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    status = models.IntegerField(choices=FetchStatus.choices, default=FetchStatus.NEEDS_FETCHING)

    class Meta:
        db_table = 'metmuse.fetchable_images'
        verbose_name_plural = "Fetchable Images"

    def __str__(self):
        return self.object_id
