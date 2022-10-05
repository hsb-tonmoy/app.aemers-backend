from rest_framework import viewsets
from apps.visa_fee_payment.serializers import VisaFeePaymentSerializer
from apps.visa_fee_payment.models import VisaFeePayment


class VisaFeePaymentViewset(viewsets.ModelViewSet):
    queryset = VisaFeePayment.objects.all()
    serializer_class = VisaFeePaymentSerializer
    lookup_field = 'user'
