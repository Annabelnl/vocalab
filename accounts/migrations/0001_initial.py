# Generated by Django 5.1.2 on 2024-11-05 22:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subscription_plan', models.CharField(choices=[('basic', 'Basic'), ('premium', 'Premium'), ('pro', 'Pro')], max_length=10)),
                ('transaction_type', models.CharField(choices=[('upgrade', 'Mise à niveau'), ('renewal', 'Renouvellement'), ('cancellation', 'Annulation')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('basic', 'Basic'), ('premium', 'Premium'), ('pro', 'Pro')], default='basic', max_length=10)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('features_included', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('fr', 'Français'), ('en', 'English'), ('nl', 'Nederlands')], default='fr', max_length=2)),
                ('notifications_enabled', models.BooleanField(default=True)),
                ('account_settings', models.JSONField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
