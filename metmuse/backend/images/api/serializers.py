from django.conf import settings

from rest_framework import serializers

from images.models import Image

CMS_HOST = settings.CMS_HOST


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(method_name="get_file")

    class Meta:
        model = Image
        fields = (
            'file', 'url', 'name', 'artist_name', 'artist_bio', 'artist_nationality', 'country', 'region', 'start_date',
            'end_date'
        )

    @staticmethod
    def get_file(obj):
        return f"{CMS_HOST}/media/{str(obj.file)}"
