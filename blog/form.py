from django import forms
from .models import Blog

class Postform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content']
