from django import forms
from .models import finding


class AddFindingUrlForm(forms.ModelForm):
    class Meta:
        model = finding
        fields = ['permalink', 'title', 'description']
        labels = {'permalink': 'adres URL',
                  'title': 'Nazwa znaleziska',
                  'description': 'Opis'}
