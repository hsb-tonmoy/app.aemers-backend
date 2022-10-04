from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.i_20_upload.views import I20Viewset

app_name = 'apps.i_20_upload'

router = DefaultRouter()

router.register(r'i_20', I20Viewset, basename='i_20_upload')

urlpatterns = [
    path('', include((router.urls))),
]
