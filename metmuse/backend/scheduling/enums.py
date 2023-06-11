from django.db import models
from django.utils.translation import gettext_lazy as _


class FetchStatus(models.IntegerChoices):
    NEEDS_FETCHING = 1, _("This image still needs to be fetched")
    BUSY_FETCHING = 2, _("This image is busy being fetched")
    FETCHED = 3, _("This image was fetched correctly")
    ERROR = 4, _("There was an error while fetching this image")
