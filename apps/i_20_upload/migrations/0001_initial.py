# Generated by Django 4.0.1 on 2022-10-04 16:46

import apps.i_20_upload.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='I_20_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=apps.i_20_upload.models.upload_to_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='i_20', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]