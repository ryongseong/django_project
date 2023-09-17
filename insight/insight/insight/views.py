from django.shortcuts import render

def home(request):
    return render(request, 'start.html')

def index(request):
    return render(request, 'mbti/main.html')

def first_question(request):
    return render(request, 'mbti/test1.html')

def second_question(request):
    return render(request, 'mbti/test2.html')

def third_question(request):
    return render(request, 'mbti/test3.html')

def fourth_question(request):
    return render(request, 'mbti/test4.html')

def fifth_question(request):
    return render(request, 'mbti/test5.html')

def six_question(request):
    return render(request, 'mbti/test6.html')

def seven_question(request):
    return render(request, 'mbti/test7.html')

def eight_question(request):
    return render(request, 'mbti/test8.html')

def nine_question(request):
    return render(request, 'mbti/test9.html')

def ten_question(request):
    return render(request, 'mbti/test10.html')

def eleven_question(request):
    return render(request, 'mbti/test11.html')

def twelve_question(request):
    return render(request, 'mbti/test12.html')