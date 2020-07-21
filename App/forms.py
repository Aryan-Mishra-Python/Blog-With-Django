from django import forms
from .models import *


"""The Post Form For The user"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'post')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'post': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


"""The Commemt Form For The User"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'comment': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
    }
