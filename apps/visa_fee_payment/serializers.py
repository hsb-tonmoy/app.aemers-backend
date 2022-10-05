from rest_framework import serializers
from apps.visa_fee_payment.models import VisaFeePayment


class VisaFeePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisaFeePayment
        fields = "__all__"
