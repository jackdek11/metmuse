from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from images.api.serializers import ImageSerializer
from images.models import Image


class ImageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (AllowAny,)
    queryset = Image.objects.all().order_by('fetchable_image')
    serializer_class = ImageSerializer
