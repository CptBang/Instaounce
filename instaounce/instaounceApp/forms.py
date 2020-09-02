from django import forms

class UploadImageForm(forms.Form):
    name = forms.CharField(max_length = 100)
    image = forms.ImageField()