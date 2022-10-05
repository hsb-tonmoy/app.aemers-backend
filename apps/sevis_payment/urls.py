from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.sevis_payment.views import SEVIS_PAYMENTViewset

app_name = 'apps.sevis_payment'

router = DefaultRouter()

router.register(r'sevis_payment', SEVIS_PAYMENTViewset,
                basename='sevis_payment')

urlpatterns = [
    path('', include((router.urls))),
]
