from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    elif request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return HttpResponse('회원가입 완료')
        else:
                 
            return HttpResponse('비밀번호 틀림')
    else:
        return HttpResponse('허용되지 않은 메소드입니다.')
    
def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('user:user')
        else:
            return HttpResponse('로그인 실패')
        
def user(request):
    return HttpResponse(request.user)