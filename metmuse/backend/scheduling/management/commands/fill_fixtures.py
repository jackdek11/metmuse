import requests
import json

from django.core.management.base import BaseCommand

from scheduling.models import Department, FetchableImages

DEPARTMENTS_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
OBJECTS_IN_DEPARTMENT_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=%s"


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Run only once to build fixtures
        """
        obj = json.loads(requests.get(DEPARTMENTS_ENDPOINT).text)
        for department in obj.get('departments'):
            Department.objects.create(id=department.get('departmentId'), name=department.get('displayName'))
        for department in Department.objects.all():
            call = OBJECTS_IN_DEPARTMENT_ENDPOINT % str(department.id)
            obj = json.loads(requests.get(call).text)
            for objectId in obj.get('objectIDs'):
                FetchableImages.objects.create(object_id=objectId, department=department)
