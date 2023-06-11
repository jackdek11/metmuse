from django.contrib import admin
from django_rq.admin import QueueAdmin
from django_rq.models import Queue


admin.site.register(Queue, QueueAdmin)
