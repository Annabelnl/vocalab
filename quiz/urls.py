from django.urls import path
from . import views

app_name = 'quiz'  # Ajoutez cette ligne pour spécifier l'espace de noms

urlpatterns = [
    path('question/', views.afficher_question, name='afficher_question'),
    path('verifier_reponse/', views.verifier_reponse, name='verifier_reponse'),
    path('signup/', views.signup, name='signup'),
]