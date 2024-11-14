from django import forms
from .models import Foto

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto', 'nome', 'descricao', 'idsitio']  # Inclua os campos necessários