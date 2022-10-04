from rest_framework import serializers
from apps.accounts.serializers import AccountsBriefSerializer
from apps.i_20_upload.models import I_20_Upload


class I20RetrieveSerializer(serializers.ModelSerializer):
    user = AccountsBriefSerializer()

    class Meta:
        model = I_20_Upload
        fields = "__all__"


class I20CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = I_20_Upload
        fields = "__all__"

    def to_representation(self, instance):
        serializer = I20RetrieveSerializer(instance)
        return serializer.data
