from django.db import models
from django.utils.translation import gettext_lazy as _


class FetchStatus(models.IntegerChoices):
    BUSY_FETCHING = 1, _("This image is busy being fetched")
    ERROR = 2, _("There was an error while fetching this image")
    FETCHED = 3, _("This image was fetched correctly")
    NEEDS_FETCHING = 4, _("This image still needs to be fetched")
