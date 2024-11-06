from django.contrib import admin
from .models import Question, UserError, Theme  # Assure-toi que les modèles sont bien importés

# Personnalisation de l'interface d'administration pour le modèle Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('mot_cible', 'phrase', 'is_cognate', 'theme')  # Colonnes à afficher dans la liste
    list_filter = ('is_cognate', 'theme')  # Ajoute des filtres sur la barre de droite pour "cognate" et "theme"
    search_fields = ('mot_cible', 'phrase')  # Ajoute un champ de recherche pour le mot cible et la phrase
    ordering = ('theme',)  # Trie par thème par défaut

# Personnalisation de l'interface d'administration pour le modèle UserError
@admin.register(UserError)
class UserErrorAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_wrong_answer', 'date')  # Colonnes à afficher dans la liste
    list_filter = ('user', 'date')  # Ajoute des filtres pour l'utilisateur et la date
    search_fields = ('user__username', 'question__phrase')  # Ajoute un champ de recherche pour l'utilisateur et la question

# Personnalisation de l'interface d'administration pour le modèle Theme
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Affiche le nom du thème
    search_fields = ('name',)  # Ajoute un champ de recherche pour le nom du thème
