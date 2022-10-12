from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.pre_departure_session.views import PreDepartureSessionViewset, ParticipantViewset

app_name = 'apps.sevis_payment'

router = DefaultRouter()

router.register(r'pre_departure_sessions', PreDepartureSessionViewset,
                basename='pre_departure_sessions')
router.register(r'pre_departure_sessions_participants', ParticipantViewset,
                basename='pre_departure_sessions_participants')

urlpatterns = [
    path('', include((router.urls))),
]
