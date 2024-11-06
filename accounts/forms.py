# accounts/forms.py

from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label="Nom d'utilisateur")
    firstname = forms.CharField(max_length=30, label="Prénom")
    lastname = forms.CharField(max_length=30, label="Nom")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.username = self.cleaned_data['username']
        user.save()
        return user


