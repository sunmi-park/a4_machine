from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    #image = models.ImageField(upload_to='', blank=True, null=True)
    pass


class ImageModel(models.Model):
    image = models.ImageField(upload_to='', blank=True, null=True)