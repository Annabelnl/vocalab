from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse  # Ajout de l'import nécessaire pour HttpResponse


def index(request):
    return render(request, 'index.html')  # Le répertoire 'templates' est déjà défini dans les settings


# Vue pour l'inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Spécifier le backend explicitement (optionnel si aucun backend personnalisé)
            login(request, user)  # backend='django.contrib.auth.backends.ModelBackend' n'est nécessaire que si tu as des backends multiples
            messages.success(request, "Votre inscription a été réalisée avec succès !")
            return redirect('index')  # Redirige vers la page d'accueil après inscription réussie
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def newsletter_signup(request):
    # Logique pour traiter l'inscription à la newsletter
    return HttpResponse("Merci de vous être inscrit à notre newsletter !")
