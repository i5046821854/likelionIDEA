from django import forms
from .models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title','writer', 'body', 'image']