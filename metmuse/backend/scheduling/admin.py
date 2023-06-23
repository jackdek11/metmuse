from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue
from django.utils.html import mark_safe

from scheduling.models import FetchableImages, FetchStatus

admin.site.register(Queue, QueueAdmin)


@admin.register(FetchableImages)
class FetchableImagesAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'status', 'indicator')

    def indicator(self, obj):
        return mark_safe(f'<div style="padding:10px;{self.get_color(obj.status)}"></div>')

    @staticmethod
    def get_color(status: FetchStatus):
        match status:
            case FetchStatus.ERROR:
                return "background-color:red;"
            case FetchStatus.FETCHED:
                return "background-color:green;"
            case FetchStatus.BUSY_FETCHING:
                return "background-color:blue;"
            case FetchStatus.NEEDS_FETCHING:
                return "background-color:grey"

