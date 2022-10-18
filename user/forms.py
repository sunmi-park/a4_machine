from django import forms
from .models import User, Photo

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','image']