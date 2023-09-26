from django.urls import path

from . import views

app_name = 'insight'

urlpatterns = [
    path('', views.index, name='index'),
    path('test1/', views.first_question, name='first_question'),
    path('test2/', views.second_question, name='second_question'),
    path('test3/', views.third_question, name='third_question'),
    path('test4/', views.fourth_question, name='fourth_question'),
    path('test5/', views.fifth_question, name='fifth_question'),
    path('test6/', views.six_question, name='six_question'),
    path('test7/', views.seven_question, name='seven_question'),
    path('test8/', views.eight_question, name='eight_question'),
    path('test9/', views.nine_question, name='nine_question'),
    path('test10/', views.ten_question, name='ten_question'),
    path('test11/', views.eleven_question, name='eleven_question'),
    path('test12/', views.twelve_question, name='twelve_question'),
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