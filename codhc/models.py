import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

#post class
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published', null=True)
    def __str__(self):
        return self.post_text, self.title, self.score, self.pub_date, self.user


#comment class
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published', null=True)
    def __str__(self):
        return self.comment_text, self.user, self.post, self.score, self.pub_date
