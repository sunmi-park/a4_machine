from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'my_user_model'
    image = models.ImageField(upload_to='', blank=True, null=True)

