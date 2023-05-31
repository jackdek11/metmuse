import requests
import json

from django.core.management.base import BaseCommand

from images.models import Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        _max = 25
        for _id in range(37, 80):
            if _max < 0:
                break
            obj = json.loads(
                        requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{_id}').text)
            if obj.get('primaryImage'):
                _max -= 1
                Image.objects.create(
                    ref=int(_id), url=obj.get('primaryImage'), name=obj.get('name'), country=obj.get('country'),
                    artistDisplayName=obj.get('artistDisplayName'), artistNationality=obj.get('artistNationality'),
                    region=obj.get('region'),
                )
