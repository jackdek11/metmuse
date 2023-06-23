from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue

from scheduling.models import FetchableImages

admin.site.register(Queue, QueueAdmin)


@admin.register(FetchableImages)
class FetchableImagesAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'status')
