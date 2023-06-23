import typing

from scheduling.models import FetchableImages, FetchStatus


def find_and_lock_image() -> typing.Optional[FetchableImages]:
    """
    This method is used to retrieve the next image to retrieve from the "stack" (FetchableImage fixtures)
    """

    # Use select_for_update() to ensure atomicity. This will lock the db row for operations
    to_fetch = FetchableImages.objects.select_for_update().filter(status=FetchStatus.NEEDS_FETCHING).first()

    if to_fetch:  # Additional check. Return None if no images from the API left
        to_fetch.status = FetchStatus.BUSY_FETCHING
        to_fetch.save(update_fields=['status'])
        return to_fetch
