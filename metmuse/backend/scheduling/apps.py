import datetime
import time


from django.apps import AppConfig
from django.conf import settings


class SchedulingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scheduling"

    def ready(self):
        if settings.RQ_SCHEDULING_INSTANCE:
            import django_rq
            from scheduling.tasks import find_images

            scheduler = django_rq.get_scheduler('image-finder')

            # Delete any existing jobs in the scheduler when the app starts up
            for job in scheduler.get_jobs():
                job.delete()

            # Schedule to get 6 more images every minute
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
            time.sleep(2)
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
            time.sleep(2)
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
            time.sleep(2)
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
            time.sleep(2)
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
            time.sleep(2)
            scheduler.schedule(datetime.datetime.utcnow(), find_images, interval=1)
