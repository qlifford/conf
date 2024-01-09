from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'title_tag', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Enter post title','class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'placeholder':'Enter post title_tag','class':'form-control'}),
            'body': forms.Textarea(attrs={'placeholder':'Post ','class':'form-control'}),
        }

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'title_tag', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control mb-3'}),
        }
