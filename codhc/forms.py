from django import forms
from django.forms import ModelForm
from codhc.models import Post, Comment

#Create the post form class
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

#Create the cadet form class
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        exclude = ['user']