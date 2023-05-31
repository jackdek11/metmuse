import json
import requests

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from django.conf import settings

from images.api.serializers import ImageSerializer
from images.models import Image, Blacklist

PAGE_SIZE = settings.PAGE_SIZE


class ImageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (AllowAny, )
    queryset = Image.objects.all().order_by('ref')
    serializer_class = ImageSerializer

    def list(self, request, *args, **kwargs):
        self.check_blacklist(request)
        return super().list(request, *args, **kwargs)

    def check_blacklist(self, request) -> None:
        total_urls = Image.objects.all().count()
        total_objects_visited = max(Image.objects.last().ref, Blacklist.objects.last().ref)
        current_page = int(request.GET.get('page'))
        if current_page * PAGE_SIZE > total_urls - PAGE_SIZE:
            self.get_more_objects(start=total_objects_visited)

    @staticmethod
    def get_more_objects(start: int) -> None:
        fetch = PAGE_SIZE * 2
        for _id in range(start +1, start + (PAGE_SIZE * 3)):
            if fetch < 0:
                break
            try:
                obj = json.loads(
                        requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{_id}').text)
            except requests.exceptions.ConnectionError:
                continue
            if obj.get('primaryImage'):
                fetch -= 1
                Image.objects.create(
                    ref=int(_id), url=obj.get('primaryImage'), name=obj.get('name'), country=obj.get('country'),
                    artistDisplayName=obj.get('artistDisplayName'), artistNationality=obj.get('artistNationality'),
                    region=obj.get('region'),
                )
            else:
                Blacklist.objects.create(ref=_id)
