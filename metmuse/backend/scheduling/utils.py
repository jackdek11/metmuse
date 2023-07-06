import typing
import logging

from PIL import Image

from django.db import transaction

from scheduling.models import FetchableImage, FetchStatus


def find_and_lock_image() -> typing.Optional[FetchableImage]:
    """
    This method is used to retrieve the next image to retrieve from the "stack" (FetchableImage fixtures)
    """

    # Use select_for_update() to ensure atomicity. This will lock the db row for operations
    with transaction.atomic():
        to_fetch = FetchableImage.objects.select_for_update().filter(status=FetchStatus.NEEDS_FETCHING).first()

        if to_fetch:  # Additional check. Return None if no images from the API left
            to_fetch.status = FetchStatus.BUSY_FETCHING
            to_fetch.save(update_fields=['status'])
            return to_fetch
        else:
            logging.error("find_and_lock_image() could not find an image")


def resize(path: str) -> None:
    image = Image.open(path)
    width = image.size[0]
    height = image.size[1]
    aspect_ratio = width / height
    target_width = 1920
    target_height = 1280
    if width > target_width or height > target_height:
        attempted_height = target_width / aspect_ratio
        target = (round(target_width), round(attempted_height))
        if attempted_height > target_height:
            attempted_width = target_height * aspect_ratio
            target = (round(attempted_width), round(target_height))
        new_image = image.resize(target)
        new_image.save(path)



