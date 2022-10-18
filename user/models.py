from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'my_user_model'
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    #pass

class Photo(models.Model):
    class Meta:
        db_table = 'img_upload'
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)