import requests
import json
import uuid
import logging

from django.core.files.temp import NamedTemporaryFile
from django.core import files
from django_rq.decorators import job

from images.models import Image

from scheduling.models import FetchableImage, SchedulingError
from scheduling.enums import FetchStatus
from scheduling.utils import find_and_lock_image

IMAGE_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects/%s"

logger = logging.getLogger('default')


@job('image-finder')
def find_images():
    obj, next_image = None, None
    try:
        next_image: FetchableImage = find_and_lock_image()
        if not next_image:
            logger.warning("No more images available")
            return
        obj = json.loads(requests.get(IMAGE_ENDPOINT % next_image.object_id).text)
        if obj.get('primaryImage'):
            response = requests.get(obj.get('primaryImage'), allow_redirects=True, stream=True)
            file_type = response.headers.get('Content-Type', default='image/jpeg').split('/')[-1].lower().strip()
            image_temp_file = NamedTemporaryFile(delete=True)
            image_temp_file.write(response.content)
            temp_file = files.File(image_temp_file, name=f"{uuid.uuid4()}.{file_type}")
            Image.objects.create(
                file=temp_file, fetchable_image=next_image, url=obj.get('primaryImage', ""), name=obj.get('title', ""),
                country=obj.get('country', ""), artist_name=obj.get('artistDisplayName', ""),
                artist_nationality=obj.get('artistNationality', ""), region=obj.get('region', ""),
                start_date=obj.get("objectBeginDate", ""), end_date=obj.get("objectEndDate", "")
            )
            image_temp_file.flush()
            temp_file.flush()
            next_image.status = FetchStatus.FETCHED
            next_image.save(update_fields=['status'])
            return
    except Exception as e:
        logger.error(e)
    if next_image:
        SchedulingError.objects.create(fetchable_image=next_image, request_response=obj or "")
        next_image.status = FetchStatus.ERROR
        next_image.save(update_fields=['status'])

