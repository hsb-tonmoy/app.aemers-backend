from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.pre_departure_session.serializers import PreDepartureSessionSerializer, ParticipantSerializer
from apps.pre_departure_session.models import PreDepartureSession, Participant


class PreDepartureSessionViewset(viewsets.ModelViewSet):
    queryset = PreDepartureSession.objects.all()
    serializer_class = PreDepartureSessionSerializer
    permission_classes = [IsAuthenticated]


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'
