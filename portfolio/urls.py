
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura/', views.licenciatura_page_view, name='licenciatura'),
    path('blog/', views.blog_page_view, name='blog'),
    path('quizz/', views.quizz_page_view, name='quizz'),
    path('projetos/', views.projetos_page_view, name='projetos'),
    path('login_page/login', views.login_page, name='login'),
    path('login_page/', views.login_page_view, name='login_page'),
    path('logout/', views.logout_page, name='logout'),
]