import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

#post class
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
    def __str__(self):
        template = '{0.post_text}{0.user}{0.title}{0.pub_date}'
        return template.format(self)


#comment class
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
    def __str__(self):
        template = '{0.comment_text}{0.user}{0.post}{0.pub_date}'
        return template.format(self)