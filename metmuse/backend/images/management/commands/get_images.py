import requests
import json
import uuid

from django.core.management.base import BaseCommand
from django.core.files.temp import NamedTemporaryFile
from django.core import files

from images.models import Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        _max = 2
        for _id in range(37, 80):
            if _max < 0:
                break
            obj = json.loads(
                requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{_id}').text)
            if obj.get('primaryImage'):
                _max -= 1
                response = requests.get(obj.get('primaryImage'), allow_redirects=True, stream=True)
                file_type = response.headers.get('Content-Type', default='image/jpeg').split('/')[-1].lower().strip()
                image_temp_file = NamedTemporaryFile(delete=True)
                image_temp_file.write(response.content)
                temp_file = files.File(image_temp_file, name=f"{uuid.uuid4()}.{file_type}")
                Image.objects.create(
                    file=temp_file,
                    ref=int(_id), url=obj.get('primaryImage'), name=obj.get('name'), country=obj.get('country'),
                    artistDisplayName=obj.get('artistDisplayName'), artistNationality=obj.get('artistNationality'),
                    region=obj.get('region'),
                )
                image_temp_file.flush()
                temp_file.flush()
