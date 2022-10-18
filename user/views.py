from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User, Photo
from django.contrib.auth import authenticate, login as loginsession
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='/user/login/')
def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def fileupload(request):
    if request.method == 'POST':
        user = User()
        user.user = request.user
        print(request.FILES["imgs"])

        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.user = user
            photo.image = img
            photo.save()
        return render(request, 'fileupload.html')

