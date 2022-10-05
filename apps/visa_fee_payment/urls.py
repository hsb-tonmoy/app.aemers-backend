from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.visa_fee_payment.views import VisaFeePaymentViewset

app_name = 'apps.visa_fee_payment'

router = DefaultRouter()

router.register(r'visa_fee_payment', VisaFeePaymentViewset,
                basename='visa_fee_payment')

urlpatterns = [
    path('', include((router.urls))),
]
