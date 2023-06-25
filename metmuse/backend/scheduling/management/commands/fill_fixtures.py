import requests
import json

from django.core.management.base import BaseCommand

from scheduling.models import FetchableImage

OBJECTS_ENDPOINT = 'https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&q=""'


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Run only once to build fixtures
        """
        obj = json.loads(requests.get(OBJECTS_ENDPOINT).text)
        for objectId in obj.get('objectIDs'):
            FetchableImage.objects.create(object_id=objectId)
