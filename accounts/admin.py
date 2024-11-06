# accounts/admin.py
from django.contrib import admin
from .models import UserPreferences, Subscription, PaymentHistory

# Pas besoin de réenregistrer le modèle User, Django le fait déjà.

# Enregistrer les autres modèles
@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'notifications_enabled']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'start_date', 'expiration_date']

@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription_plan', 'amount', 'transaction_type', 'date']
