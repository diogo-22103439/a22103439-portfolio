from django.db import models

# Create your models here.

class Cadeira(models.Model):
   nome = models.CharField(max_length=30, unique=True)
   ano = models.IntegerField()
   semetre = models.IntegerField()
   ects = models.IntegerField()

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    autor = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    pontuacao = models.PositiveIntegerField()

class Projeto(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo