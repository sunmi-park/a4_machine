from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('fileUpload/', views.test, name='test'),
    
]