from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PreApplicationFormViewset

app_name = 'apps.pre_application_form'

router = DefaultRouter()

router.register(r'pre_application_form',
                PreApplicationFormViewset, basename='pre_application_form')

urlpatterns = [
    path('', include((router.urls))),
]
