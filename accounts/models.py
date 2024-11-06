# accounts/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import path
from django.contrib.auth.views import LoginView

# Modèle de préférences utilisateur
class UserPreferences(models.Model):
    LANGUAGE_CHOICES = [
        ('fr', _('Français')),
        ('en', _('English')),
        ('nl', _('Nederlands')),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='fr')
    notifications_enabled = models.BooleanField(default=True)
    account_settings = models.JSONField(null=True, blank=True)  # Pour des paramètres supplémentaires, au besoin

    def __str__(self):
        return f"Préférences de {self.user.username}"

# Modèle d'abonnement
class Subscription(models.Model):
    PLAN_CHOICES = [
        ('basic', _('Basic')),
        ('premium', _('Premium')),
        ('pro', _('Pro')),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subscription")
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default='basic')
    start_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    features_included = models.JSONField()  # Liste des fonctionnalités incluses

    def __str__(self):
        return f"Abonnement de {self.user.username} - {self.plan}"

# Historique des paiements et des abonnements
class PaymentHistory(models.Model):
    TRANSACTION_CHOICES = [
        ('upgrade', _('Mise à niveau')),
        ('renewal', _('Renouvellement')),
        ('cancellation', _('Annulation')),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_history")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    subscription_plan = models.CharField(max_length=10, choices=Subscription.PLAN_CHOICES)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)

    def __str__(self):
        return f"Paiement de {self.user.username} - {self.subscription_plan} - {self.date.strftime('%Y-%m-%d')}"

# URL pour la vue de connexion
urlpatterns = [
    path('signin/', LoginView.as_view(template_name='accounts/login.html'), name='signin'),
]
