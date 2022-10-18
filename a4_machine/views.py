from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')