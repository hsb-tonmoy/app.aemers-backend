from rest_framework import viewsets
from apps.i_20_upload.serializers import I20RetrieveSerializer, I20CreateSerializer
from apps.i_20_upload.models import I_20_Upload


class I20Viewset(viewsets.ModelViewSet):
    queryset = I_20_Upload.objects.all()
    serializer_class = I20CreateSerializer
    lookup_field = 'user'

    retrieve_serializer_class = I20RetrieveSerializer

    def get_serializer_class(self):

        if self.action == 'retrieve':
            if hasattr(self, 'retrieve_serializer_class'):
                return self.retrieve_serializer_class

        return super(I20Viewset, self).get_serializer_class()
