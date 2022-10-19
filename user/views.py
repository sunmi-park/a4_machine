from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User, Image
from django.contrib.auth import authenticate, login as loginsession
from .forms import FileUploadForm
from a4_machine.machine import find_something

# Create your views here.

def signup(request):
    if request.method=='GET':
        return render(request, 'user/signup.html')
    elif request.method=='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('/login/')
        else:
            return HttpResponse('비밀번호 틀림')
    else:
        return HttpResponse('허용되지 않은 메소드입니다.')

def login(request):
    if request.method=='GET':
        return render(request, 'user/login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('/')
        else:
            return HttpResponse('로그인 실패')

def main(request):
    if request.method == 'POST':
        username = request.user
        img_file = request.FILES.get('image')
        img = Image()
        img.username = username
        img.image = img_file
        img.user = username
        img.save()
        img_name = img.image.url
        find_something(request, img_name)

        return redirect('/fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'user/main.html', context)

def fileupload(request):
    if request.method == "GET":
        imgs = {
            'result.png'
        }
        return render(request, 'user/fileupload.html', imgs=imgs)

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/login')
