from django import forms

class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	

class InscriptionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	email = forms.EmailField(label="Votre adresse mail")
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

# Create your models here.
