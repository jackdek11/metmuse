from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue

from images.models import Image


admin.site.register(Image)
admin.site.register(Queue, QueueAdmin)