from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.mock_visa_interview.views import MockVisaInterviewQuestionViewset, MockVisaInterviewSessionViewset, MockVisaInterviewAnswerViewset

app_name = 'apps.mock_visa_interview'

router = DefaultRouter()

router.register(r'mock_visa_interview_session', MockVisaInterviewSessionViewset,
                basename='mock_visa_interview_session')
router.register(r'mock_visa_interview_question',
                MockVisaInterviewQuestionViewset, basename='mock_visa_interview_question')

router.register(r'mock_visa_interview_answer',
                MockVisaInterviewAnswerViewset, basename='mock_visa_interview_answer')

urlpatterns = [
    path('', include((router.urls))),
]
