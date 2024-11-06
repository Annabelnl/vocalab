# vocalab/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Importation correcte des vues
from django.conf import settings  # Nécessaire pour accéder aux paramètres
from django.conf.urls.static import static  # Nécessaire pour servir les fichiers médias en développement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),  # URLs pour votre application quiz
    path('', views.index, name='index'),  # Utilise views.index pour la page d'accueil
    path('accounts/', include('allauth.urls')),  # Inclure toutes les URLs d'authentification d'allauth
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),  # URL pour l'inscription à la newsletter
]

# Ajoutez cette partie pour servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
