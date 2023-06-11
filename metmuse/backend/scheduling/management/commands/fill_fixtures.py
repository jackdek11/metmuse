import requests
import json

from django.core.management.base import BaseCommand

from scheduling.models import Department


class Command(BaseCommand):

    def handle(self, *args, **options):
        _max = 2
        obj = json.loads(
            requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments').text)
        for department in obj.get('departments'):
            Department.objects.create(id=department.get('departmentId'), name=department.get('displayName'))
