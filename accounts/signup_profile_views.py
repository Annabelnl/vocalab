from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Utiliser authenticate() pour récupérer l'utilisateur avec le backend correct
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Si l'utilisateur est authentifié correctement, alors le connecter
            if user is not None:
                login(request, user)
                messages.success(request, "Votre compte a été créé avec succès !")
                return redirect('index')  # Redirection vers la page d'accueil après inscription

        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
