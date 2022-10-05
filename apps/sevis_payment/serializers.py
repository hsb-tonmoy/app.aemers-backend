from rest_framework import serializers
from apps.sevis_payment.models import SEVIS_PAYMENT


class SEVIS_PAYMENTSerializer(serializers.ModelSerializer):

    class Meta:
        model = SEVIS_PAYMENT
        fields = "__all__"
