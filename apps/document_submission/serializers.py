from rest_framework import serializers
from apps.accounts.serializers import AccountsBriefSerializer
from .models import Document, DocumentCategory


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"


class DocumentListSerializer(serializers.ModelSerializer):
    checked_by = AccountsBriefSerializer()
    user = AccountsBriefSerializer()
    category = DocumentCategorySerializer()

    class Meta:
        model = Document
        fields = "__all__"


class DocumentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = "__all__"

    def to_representation(self, instance):
        serializer = DocumentListSerializer(instance)
        return serializer.data
