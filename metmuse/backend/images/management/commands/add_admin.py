from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings

UserModel = get_user_model()

ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD
ADMIN_EMAIL = settings.ADMIN_EMAIL


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not UserModel.objects.filter(Q(username=ADMIN_USERNAME) | Q(email=ADMIN_EMAIL)).exists():
            UserModel.objects.create_superuser(
                username=ADMIN_USERNAME, email=ADMIN_EMAIL, password=ADMIN_PASSWORD
            )
