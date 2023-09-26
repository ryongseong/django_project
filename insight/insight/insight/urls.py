from django.urls import path

from . import views

app_name = 'insight'

urlpatterns = [
    path('', views.mbti_test, name='mbti_test'),
    path('ENFJ/', views.ENFJ, name='ENFJ'),
    path('ENFP/', views.ENFP, name='ENFP'),
    path('ENTJ/', views.ENTJ, name='ENTJ'),
    path('ENTP/', views.ENTP, name='ENTP'),
    path('ESFJ/', views.ESFJ, name='ESFJ'),
    path('ESFP/', views.ESFP, name='ESFP'),
    path('ESTJ/', views.ESTJ, name='ESTJ'),
    path('ESTP/', views.ESTP, name='ESTP'),
    path('INFJ/', views.INFJ, name='INFJ'),
    path('INFP/', views.INFP, name='INFP'),
    path('INTJ/', views.INTJ, name='INTJ'),
    path('INTP/', views.INTP, name='INTP'),
    path('ISFJ/', views.ISFJ, name='ISFJ'),
    path('ISFP/', views.ISFP, name='ISFP'),
    path('ISTJ/', views.ISTJ, name='ISTJ'),
    path('ISTP/', views.ISTP, name='ISTP'),
]