from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.views import AccountsViewset, ApplicationStatusViewset, ClientFollowingViewset, NotificationViewset

app_name = 'apps.accounts'

router = DefaultRouter()

router.register(r'accounts', AccountsViewset, basename='accounts')
router.register(r'application_status', ApplicationStatusViewset,
                basename='application_status')
router.register(r'clientfollowing', ClientFollowingViewset,
                basename='clientfollowing')
router.register(r'notifications', NotificationViewset,
                basename='notifications')

urlpatterns = [
    path('', include((router.urls))),
]
