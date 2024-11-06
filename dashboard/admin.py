from django.contrib import admin
from .models import UserProgress, Badge, UserQuizHistory, UserGoal

# Enregistrement des modèles pour l'administration
admin.site.register(UserProgress)
admin.site.register(Badge)
admin.site.register(UserQuizHistory)
admin.site.register(UserGoal)
