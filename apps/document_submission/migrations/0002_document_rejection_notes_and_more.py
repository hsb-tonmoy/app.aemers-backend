# Generated by Django 4.1.3 on 2022-11-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_submission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='rejection_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='rejection_notes',
            field=models.TextField(blank=True),
        ),
    ]
