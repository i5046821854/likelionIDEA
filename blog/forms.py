from django import forms
from .models import blog
from list.models import list

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'detail', 'image']

        
class listForm(forms.ModelForm):
    class Meta:
        model = list
        fields = ['name','share', 'icon']