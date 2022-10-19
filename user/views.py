from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User, ImageModel
from django.contrib.auth import authenticate, login as loginsession
from .forms import FileUploadForm
import torch
from django.conf import settings

# Create your views here.

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
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
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('/main/')
        else:
            return HttpResponse('로그인 실패')

def main(request):
    if request.method =='GET':
        return render(request, 'main.html')

    if request.method == 'POST':
       
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid(): # 사진 업로드 유효성검사
            form.save()
            form.instance.image
            

            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True) # yolo 모델
            results = model([settings.BASE_DIR / form.instance.image.url[1:]]) 
            results.save(model, 'media', True) # media yolo파일로 덮음
            
        
        context = {
            'form': form
            
        }
        return render(request, 'fileUpload.html', context)


def fileupload(request):
    if request.method == "GET":
        return render(request, 'fileupload.html')
