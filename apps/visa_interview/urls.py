from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.visa_interview.views import VisaInterviewViewset

app_name = 'apps.visa_interview'

router = DefaultRouter()

router.register(r'visa_interview', VisaInterviewViewset,
                basename='visa_interview')

urlpatterns = [
    path('', include((router.urls))),
]
