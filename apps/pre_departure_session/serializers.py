from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.pre_departure_session.models import PreDepartureSession, Participant


class PreDepartureSessionSerializer(ModelSerializer):
    time = SerializerMethodField()

    def get_time(self, obj):
        return obj.time.strftime("%I:%M %p")

    class Meta:
        model = PreDepartureSession
        fields = "__all__"


class ParticipantSerializer(ModelSerializer):
    pre_departure_session = PreDepartureSessionSerializer()

    class Meta:
        model = Participant
        fields = "__all__"
