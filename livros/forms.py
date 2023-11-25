from django import forms
from django.forms import ModelForm
from .models import Livro, Review

class LivroForm(forms.Form):
    name = forms.CharField(label='Título', max_length=100)
    release_year = forms.IntegerField(label='Data de Lançamento',
                                      min_value=1888)
    poster_url = forms.URLField(label='URL do Poster', max_length=100)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }