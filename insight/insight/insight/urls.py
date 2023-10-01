from django.urls import path

from . import views

app_name = 'insight'

urlpatterns = [
    path('', views.mbti_test_main, name='mbti_test_main'),
    path('mbti/', views.mbti_test, name='mbti_test'),
    path('mbti/ENFJ/', views.ENFJ, name='ENFJ'),
    path('mbti/ENFP/', views.ENFP, name='ENFP'),
    path('mbti/ENTJ/', views.ENTJ, name='ENTJ'),
    path('mbti/ENTP/', views.ENTP, name='ENTP'),
    path('mbti/ESFJ/', views.ESFJ, name='ESFJ'),
    path('mbti/ESFP/', views.ESFP, name='ESFP'),
    path('mbti/ESTJ/', views.ESTJ, name='ESTJ'),
    path('mbti/ESTP/', views.ESTP, name='ESTP'),
    path('mbti/INFJ/', views.INFJ, name='INFJ'),
    path('mbti/INFP/', views.INFP, name='INFP'),
    path('mbti/INTJ/', views.INTJ, name='INTJ'),
    path('mbti/INTP/', views.INTP, name='INTP'),
    path('mbti/ISFJ/', views.ISFJ, name='ISFJ'),
    path('mbti/ISFP/', views.ISFP, name='ISFP'),
    path('mbti/ISTJ/', views.ISTJ, name='ISTJ'),
    path('mbti/ISTP/', views.ISTP, name='ISTP'),
]