# Generated by Django 4.0.1 on 2022-10-13 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFileOpeningPaymentAmount',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('payment_amount', models.CharField(max_length=255, verbose_name='Payment Amount')),
                ('modified_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('checked_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Payment Amount',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFileOpening',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Method')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment ID')),
                ('payment_amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Amount')),
                ('payment_currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Currency')),
                ('submitted', models.BooleanField(default=False, verbose_name='Submitted')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Payment Info',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='FileOpeningPaymentAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.CharField(max_length=255, verbose_name='Payment Amount')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_opening_checked_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_opening_payment_amount', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment Amount',
                'verbose_name_plural': 'Payment Payment',
            },
        ),
        migrations.CreateModel(
            name='FileOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Method')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment ID')),
                ('payment_amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Amount')),
                ('payment_currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment Currency')),
                ('submitted', models.BooleanField(default=False, verbose_name='Submitted')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_opening_payment_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment Info',
                'verbose_name_plural': 'Payment Info',
            },
        ),
    ]