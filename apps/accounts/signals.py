from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.template.loader import get_template
from post_office import mail
from .utils import generate_unique_username
from .models import Profile
import datetime
import pytz
import sys

User = get_user_model()


@receiver(post_save, sender=User)
def username_add(sender, instance, created, **kwargs):
    if created:
        if instance.first_name and instance.last_name:
            username = generate_unique_username(
                instance.first_name + instance.last_name)
        else:
            return
        instance.username = username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def add_or_update_user_group(sender, instance, created, **kwargs):
    if created:
        group = None
        if instance.account_type == 1:
            if not Group.objects.filter(name="Visitors").exists():
                Group.objects.create(name="Visitors")
            group = Group.objects.get(name="Visitors")

        elif instance.account_type == 2:
            if not Group.objects.filter(name="Clients").exists():
                Group.objects.create(name="Clients")
            group = Group.objects.get(name="Clients")

        elif instance.account_type == 3:
            if not Group.objects.filter(name="Consultants").exists():
                Group.objects.create(name="Consultants")
            group = Group.objects.get(name="Consultants")

        elif instance.account_type == 4:
            if not Group.objects.filter(name="Managers").exists():
                Group.objects.create(name="Managers")
            group = Group.objects.get(name="Managers")

        elif instance.account_type == 5:
            if not Group.objects.filter(name="Admins").exists():
                Group.objects.create(name="Admins")
            group = Group.objects.get(name="Admins")

        instance.groups.add(group)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):

    if created and not (len(sys.argv) > 1 and sys.argv[1] == 'runserver'):

        current_time = datetime.datetime.now()

        current_time = current_time.astimezone(
            pytz.timezone('US/Eastern')).strftime('%d %B %Y %I:%M %p')

        context = {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'date_time': current_time,
        }

        template = get_template(
            'accounts/welcome-email.html').render(context)

        mail.send([instance.email], "Mamoon Rashid <no-reply@aemers.com>", subject="Welcome to app.aemers.com",
                  html_message=template, priority='now')
