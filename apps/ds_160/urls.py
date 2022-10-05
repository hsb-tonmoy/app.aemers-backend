from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.ds_160.views import DS160Viewset

app_name = 'apps.ds_160'

router = DefaultRouter()

router.register(r'ds_160', DS160Viewset, basename='ds_160')

urlpatterns = [
    path('', include((router.urls))),
]
