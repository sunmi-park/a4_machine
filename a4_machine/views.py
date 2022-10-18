from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from user.models import User, Photo

@login_required(login_url='/user/login/')
def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    
def fileupload(request):
    if request.mothod == 'POST':
        user = User()
        user.user = request.user
        user.save()
        
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.user = user
            photo.image = img
            photo.save()
        return redirect('/test/' + str(user.id))
    
        