from django.shortcuts import render

def mbti_test(request):
    return render(request, 'test.html')

def home(request):
    return render(request, 'start.html')

def ENFJ(request):
    return render(request, 'result/ENFJ.html')

def ENFP(request):
    return render(request, 'result/ENFP.html')

def ENTJ(request):
    return render(request,'result/ENTJ.html')

def ENTP(request):
    return render(request, 'result/ENTP.html')

def ESFJ(request):
    return render(request, 'result/ESFJ.html')

def ESFP(request):
    return render(request, 'result/ESFP.html')

def ESTJ(request):
    return render(request, 'result/ESTJ.html')

def ESTP(request):
    return render(request, 'result/ESTP.html')

def INFJ(request):
    return render(request, 'result/INFJ.html')

def INFP(request):
    return render(request, 'result/INFP.html')

def INTJ(request):
    return render(request, 'result/INTJ.html')

def INTP(request):
    return render(request, 'result/INTP.html')

def ISFJ(request):
    return render(request, 'result/ISFJ.html')

def ISFP(request):
    return render(request, 'result/ISFP.html')

def ISTJ(request):
    return render(request, 'result/ISTJ.html')

def ISTP(request):
    return render(request, 'result/ISTP.html')