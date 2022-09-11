import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

from notifications.models import Notification

from apps.accounts.models import Accounts, ApplicationStatus, Profile, ClientFollowing
from apps.accounts.serializers import AccountsListSerializer, AccountsUpdateSerializer, ApplicationStatusSerializer, ClientFollowingSerializer, NotificationSerializer
from apps.accounts.permissions import OnlyAdminandStaffCanRetrieve

GOOGLE_OAUTH_CALLBACK_URL = settings.GOOGLE_OAUTH_CALLBACK_URL


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class AccountsViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsUpdateSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, OnlyAdminandStaffCanRetrieve]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', ]
    lookup_field = 'username'
    list_serializer_class = AccountsListSerializer
    update_serializer_class = AccountsUpdateSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        elif self.action == 'update' or self.action == 'partial_update':
            if hasattr(self, 'update_serializer_class'):
                return self.update_serializer_class

        return super(AccountsViewset, self).get_serializer_class()


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()


class ApplicationStatusViewset(viewsets.ModelViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'


class ClientFollowingViewset(viewsets.ModelViewSet):
    queryset = ClientFollowing.objects.all()
    serializer_class = ClientFollowingSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('manager',)


class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        user = self.request.user
        queryset = user.notifications.unread()
        if params.get('markAsRead') == 'true':
            queryset.mark_all_as_read()
        if params.get('all') == 'true':
            read_notifications = user.notifications.read()
            return queryset | read_notifications
        return queryset
