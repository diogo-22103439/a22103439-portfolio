from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
import datetime
from matplotlib import pyplot as plt

from .models import *
from .forms import *

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/")

    return redirect("/login_page")

def logout_page(request):
    logout(request)
    return redirect("/login_page")


def login_page_view(request):
    return render(request, "portfolio/login.html")


def home_page_view(request):
    agora = datetime.datetime.now()
    context = {
        'hora': agora.hour,
    }
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    context = {
        'cadeiras':Cadeira.objects.all()
    }
    return render(request, 'portfolio/licenciatura.html', context)


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

    if request.POST['pergunta1'] == 'op2':
        pontos += 25
    if request.POST['pergunta2'] == 'op3':
        pontos += 25
    if request.POST['pergunta3'] == 'op3':
        pontos += 25
    if request.POST['pergunta4'] == 'op1':
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

def projetos_page_view(request):
    context = {
        'projetos':Projeto.objects.all()
    }
    return render(request, 'portfolio/projetos.html', context)