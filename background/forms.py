from django import forms
from .models import Background


class BackgroundForm(forms.ModelForm):
    class Meta:
        model = Background
        fields = ("titre","sujet","histoire")
