from django.shortcuts import render
import datetime
from matplotlib import pyplot as plt

from .models import *
from .forms import *


def home_page_view(request):
    agora = datetime.datetime.now()
    context = {
        'hora': agora.hour,
    }
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def blog_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'posts': Post.objects.all(),
        'form': form
    }

    return render(request, 'portfolio/blog.html', context)


def pontuacao_quizz(request):
    pontos = 0

    if request.POST['pergunta1'] == 'respostaCerta':
        pontos += 25
    if request.POST['pergunta2'] == 'respostaCerta':
        pontos += 25
    if request.POST['pergunta3'] == 'respostaCerta':
        pontos += 25
    if request.POST['pergunta4'] == 'respostaCerta':
        pontos += 25

    return pontos


def desenha_grafico_pontos():
    bd_ordenada = sorted(PontuacaoQuizz.objects.all(), key=lambda o: o.pontuacao, reverse=True)
    nomes = [objeto.nome for objeto in bd_ordenada]
    pontos = [objeto.pontuacao for objeto in bd_ordenada]
    plt.barh(nomes, pontos)
    plt.savefig('portfolio/static/portfolio/images/resultados.png', bbox_inches='tight')
    plt.close()


def quizz_page_view(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pontos = pontuacao_quizz(request)
        PontuacaoQuizz.objects.update_or_create(nome=nome,defaults={'pontuacao':pontos})
        desenha_grafico_pontos()

    return render(request, 'portfolio/quizz.html')
