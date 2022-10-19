from django.urls import path
from user import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('',views.home)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
