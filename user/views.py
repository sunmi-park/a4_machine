from django.contrib import auth
from django.shortcuts import redirect, render
from .models import User, Image
from django.contrib.auth import authenticate, login as loginsession
from .forms import FileUploadForm
from a4_machine.machine import find_something
import re
# Create your views here.

def signup(request):
    if request.method=='GET':
        return render(request, 'user/signup.html')
    elif request.method=='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        is_email = re.compile(r"^[a-zA-Z]+[!#$%&'*+-/=?^_`(){|}~]*[a-zA-Z0-9]*@[\w]+\.[a-zA-Z0-9-]+[.]*[a-zA-Z0-9]+$")
        if password != passwordcheck:
            return render(request, 'user/signup.html', {'error': '비밀번호가 맞지 않습니다!'})
        elif username.replace(' ','') == '':
            return render(request, 'user/signup.html', {'error': 'username은 공백일 수 없습니다!'})
        elif is_email.match(email) == False:
            return render(request, 'user/signup.html', {'error': 'email을 확인해 주세요!'})
        elif password == passwordcheck:
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('/login/')
    else:
        return render(request, 'user/signup.html', {'error': '아이디와 비밀번호를 확인해 주세요!'})

def login(request):
    if request.method=='GET':
        return render(request, 'user/login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            loginsession(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error': '아이디와 비밀번호를 확인해 주세요!'})

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
        return render(request, 'user/fileupload.html')


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/login')
