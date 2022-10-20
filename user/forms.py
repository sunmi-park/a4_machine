from django import forms
from .models import ImageModel

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']

