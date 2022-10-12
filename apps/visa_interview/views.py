from rest_framework import viewsets
from apps.visa_interview.serializers import VisaInterviewSerializer
from apps.visa_interview.models import VisaInterview


class VisaInterviewViewset(viewsets.ModelViewSet):
    queryset = VisaInterview.objects.all()
    serializer_class = VisaInterviewSerializer
    lookup_field = 'user'
