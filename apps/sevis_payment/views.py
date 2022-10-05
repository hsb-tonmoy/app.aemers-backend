from rest_framework import viewsets
from apps.sevis_payment.serializers import SEVIS_PAYMENTSerializer
from apps.sevis_payment.models import SEVIS_PAYMENT


class SEVIS_PAYMENTViewset(viewsets.ModelViewSet):
    queryset = SEVIS_PAYMENT.objects.all()
    serializer_class = SEVIS_PAYMENTSerializer
    lookup_field = 'user'
