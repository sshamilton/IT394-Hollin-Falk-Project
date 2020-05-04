from django import forms
from django.forms import ModelForm
from codhc.models import Post, Comment

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#Create the form class
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'score', 'title', 'post_text', 'pub_date']

#Create form to add a Post
PostForm = PostForm()

#Create the form class
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'score', 'comment_text', 'pub_date']

#Create form to add a Post
CommentForm = CommentForm()