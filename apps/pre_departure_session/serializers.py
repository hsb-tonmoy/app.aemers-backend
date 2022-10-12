from rest_framework.serializers import ModelSerializer
from apps.pre_departure_session.models import PreDepartureSession, Participant


class PreDepartureSessionSerializer(ModelSerializer):
    class Meta:
        model = PreDepartureSession
        fields = "__all__"


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"
