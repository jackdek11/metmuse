""" URLS for Lists """
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from images.api.viewsets import ImageViewSet


router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='lists')

urlpatterns = [
    path('', include(router.urls))
]
