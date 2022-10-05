from rest_framework import viewsets
from apps.ds_160.serializers import DS160Serializer
from apps.ds_160.models import DS160


class DS160Viewset(viewsets.ModelViewSet):
    queryset = DS160.objects.all()
    serializer_class = DS160Serializer
    lookup_field = 'user'
