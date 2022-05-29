
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura/', views.licenciatura_page_view, name='licenciatura'),
    path('blog/', views.blog_page_view, name='blog'),
    path('quizz/', views.quizz_page_view, name='quizz'),
]