from django import forms
from .models import Profil

class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class InscriptionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	prenom = forms.CharField(label="Prenom", max_length=30, required=False)
	nom = forms.CharField(label="nom de famille", max_length=30, required=False)
	email = forms.EmailField(label="Votre adresse mail", required=False)


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ('user', 'personnagePrincipal')


