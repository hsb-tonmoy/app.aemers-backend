from rest_framework import serializers
from apps.ds_160.models import DS160


class DS160Serializer(serializers.ModelSerializer):

    class Meta:
        model = DS160
        fields = "__all__"
