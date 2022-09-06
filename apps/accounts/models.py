from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from simple_history.models import HistoricalRecords

from apps.accounts.utils import random_username
from random import randint
from apps.accounts.managers import AccountsManager


def upload_to_path(instance, filename):
    extension = filename.split(".")[-1].lower()
    file_id = randint(10000000, 99999999)
    path = f'profiles/{file_id}_{instance.last_name}.png'
    return path


class Accounts(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["id"]

    objects = AccountsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    history = HistoricalRecords()

    # General fields

    email = models.EmailField(_('Email Address'), unique=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),

        },
        blank=True,
        default=random_username
    )

    first_name = models.CharField(_('First name'), max_length=150, blank=True)
    last_name = models.CharField(_('Last name'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USER_TYPE_CHOICES = (
        (1, 'Visitor'),
        (2, 'Client'),
        (3, 'Consultant'),
        (4, 'Manager'),
        (5, 'Admin'),
        (6, 'SuperAdmin'),
    )

    account_type = models.PositiveSmallIntegerField(
        _("Account Type"), choices=USER_TYPE_CHOICES, default=1)

    # Model methods

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


EP_CHOICES = (
    ('ielts', 'IELTS'),
    ('toefl', 'TOEFL'),
    ('duolingo', 'Duolingo'),
    ('no-test', 'Wish to get enrolled without any test'),
    ('moi', 'Wish to get enrolled with Medium Of Instruction'),
    ('plan-to', 'Wish to take IELTS'),)


STATUS_CHOICES = (
    (0, "Default"),
    (1, "Package Sent"),
    (2, "Converted"),
    (3, "Follow-up"),
    (4, "Muted"),
)

PRIORITY_RATINGS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class Profile(models.Model):

    user = models.OneToOneField(
        Accounts, on_delete=models.CASCADE, related_name="profile")

    profile_pic = ProcessedImageField(upload_to=upload_to_path,
                                      processors=[ResizeToFill(270, 270)],
                                      format='PNG',
                                      options={'quality': 60}, default='profiles/avatar.png', null=True, blank=True)

    # Personal Information

    country = models.CharField(
        _("Country"), max_length=255, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=255, null=True, blank=True)

    # Degree

    degree = models.CharField(
        _("Degree"), max_length=255, null=True, blank=True)

    # Major

    major = models.CharField(_("Major"), max_length=255, null=True, blank=True)

    # English Proficiency

    english_proficiency = models.CharField(
        _("English Proficiency"), max_length=15, choices=EP_CHOICES, default='ielts')

    english_proficiency_score = models.CharField(
        _("Score"), max_length=255, blank=True, null=True)

    # Message

    message = models.TextField(
        _("Message"), blank=True, null=True)

    # Manager Fields

    status = models.PositiveSmallIntegerField(
        _("Status"), choices=STATUS_CHOICES, default=0)

    rating = models.PositiveSmallIntegerField(
        _("Rating"), choices=PRIORITY_RATINGS, default=1)

    # Internal Fields

    isEvaluated = models.BooleanField(default=False)
    isNewApplicant = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


STEP_STATUS = (
    (0, "Pending"),
    (1, "Started"),
    (2, "Complete"),
)


class ApplicationStatus(models.Model):
    class Meta:
        verbose_name = _("Application Status")
        verbose_name_plural = _("Application Statuses")
        ordering = ["id"]

    history = HistoricalRecords()

    # General fields

    user = models.OneToOneField(
        Accounts, on_delete=models.CASCADE, related_name="application")

    # Application Steps

    application_started = models.BooleanField(
        _("Application Started?"), default=False)
    file_opening = models.PositiveSmallIntegerField(
        _("File Opening"), choices=STEP_STATUS, default=0)
    orientation = models.PositiveSmallIntegerField(
        _("Orientation"), choices=STEP_STATUS, default=0)
    pre_application_form = models.PositiveSmallIntegerField(
        _("Pre-Application Form"), choices=STEP_STATUS, default=0)
    documents_upload = models.PositiveSmallIntegerField(
        _("Documents Upload"), choices=STEP_STATUS, default=0)
    i_20_upload = models.PositiveSmallIntegerField(
        _("I-20 Upload"), choices=STEP_STATUS, default=0)
    ds_160_filed = models.PositiveSmallIntegerField(
        _("DS-160 Filed"), choices=STEP_STATUS, default=0)
    sevis_payment = models.PositiveSmallIntegerField(
        _("SEVIS Payment"), choices=STEP_STATUS, default=0)
    visa_fee_payment = models.PositiveSmallIntegerField(
        _("Visa Fee Payment"), choices=STEP_STATUS, default=0)
    visa_interview = models.PositiveSmallIntegerField(
        _("Visa Interview"), choices=STEP_STATUS, default=0)
    pre_departure_session = models.PositiveSmallIntegerField(
        _("Pre-Departure Session"), choices=STEP_STATUS, default=0)
    welcome_to_usa = models.PositiveSmallIntegerField(
        _("Welcome to USA"), choices=STEP_STATUS, default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ClientFollowing(models.Model):
    manager = models.ForeignKey(
        Accounts, related_name="clients", on_delete=models.CASCADE)
    client = models.ForeignKey(
        Accounts, related_name="managers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['manager', 'client'],  name="unique_followers")
        ]

        ordering = ["-created"]

    def __str__(self):
        return f'{self.manager.first_name} following {self.client.first_name}'
