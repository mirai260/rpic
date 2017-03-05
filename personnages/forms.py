from django import forms
from .models import Perso, FichePerso

class PersoForm(forms.ModelForm):
	class Meta:
		model = Perso
		fields = ('nom', 'image')

class FichePersoForm(forms.ModelForm):
	class Meta:
		model = FichePerso
		#fields = '__all__'
		exclude = ('perso', 'extra', 'item')