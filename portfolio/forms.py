from django import forms
from django.forms import ModelForm
from .models import Post, Cadeira, Projeto


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        labels = {
            'titulo': 'Título:',
            'descricao': 'Texto:'
        }

class PostFormLicenciatura(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        labels = {
            'titulo': 'Título:',
            'descricao': 'Texto:'
        }


class PostFormProject(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        labels = {
            'titulo': 'Título:',
            'descricao': 'Texto:'
        }