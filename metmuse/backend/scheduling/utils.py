import typing
import logging

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
