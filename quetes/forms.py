from django import forms
from .models import Quete


class QueteForm(forms.ModelForm):
    class Meta:
        model = Quete
        exclude = ('participants',)