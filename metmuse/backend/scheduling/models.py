from django.db import models
from scheduling.enums import FetchStatus


class FetchableImage(models.Model):
    object_id = models.IntegerField()
    status = models.IntegerField(choices=FetchStatus.choices, default=FetchStatus.NEEDS_FETCHING)

    class Meta:
        db_table = 'metmuse.fetchable_images'
        verbose_name_plural = "Fetchable Images"

    def __str__(self):
        return str(self.object_id)


class SchedulingError(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    fetchable_image = models.ForeignKey(FetchableImage, on_delete=models.CASCADE)
    retries = models.IntegerField(default=0)
    request_response = models.JSONField(blank=True)

    class Meta:
        db_table = 'metmuse.scheduling_errror'
        verbose_name_plural = "Scheduling Errors"

    def __str__(self):
        return f"Fetchable Image: {str(self.fetchable_image.object_id)}| retries: {str(self.retries)}"
