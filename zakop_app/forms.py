from django import forms
from .models import Finding


class AddFindingUrlForm(forms.ModelForm):
    class Meta:
        model = Finding
        fields = ['permalink', 'title', 'description']
        labels = {'permalink': 'adres URL',
                  'title': 'Nazwa znaleziska',
                  'description': 'Opis'}
