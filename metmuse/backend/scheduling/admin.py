from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue

from scheduling.models import Department, FetchableImages

admin.site.register(Queue, QueueAdmin)
admin.site.register(Department)


@admin.register(FetchableImages)
class FetchableImagesAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'department', 'status')
