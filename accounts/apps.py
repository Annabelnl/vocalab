# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Placez ici tout code de démarrage que vous souhaitez exécuter au démarrage de l'application
        pass
