<<<<<<< HEAD
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from user.models import User, Photo


def main(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'main.html')
        else:
            return redirect('/login')
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

=======
>>>>>>> d6f830cad1275fef56954c8063344d72242d096e
