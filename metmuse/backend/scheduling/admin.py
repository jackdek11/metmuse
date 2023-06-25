from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue
from django.db import models
from django.utils.html import mark_safe
from django_json_widget.widgets import JSONEditorWidget
from django.urls import reverse

from scheduling.models import FetchableImage, SchedulingError
from scheduling.enums import FetchStatus

admin.site.register(Queue, QueueAdmin)


@admin.register(FetchableImage)
class FetchableImageAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'status', 'last_response')
    list_filter = ("status",)

    @staticmethod
    def last_response(obj):
        try:
            last_response = obj.schedulingerror_set.last()
            if not last_response:
                return None
            detail = f"[{last_response.created_on}]"
            return mark_safe(
                f'<a href="{reverse("admin:scheduling_schedulingerror_change", args=(last_response.id,))}">{detail}</a>'
            )
        except AttributeError:
            return None

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


@admin.register(SchedulingError)
class SchedulingErrorAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'fetchable_image', 'retries')
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }
