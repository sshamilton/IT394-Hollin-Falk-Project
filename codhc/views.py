from django.shortcuts import render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.

def index(request):
    latest_post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'codhc/index.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id, pub_date__lte=timezone.now())
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'codhc/detail.html', {'post': post})

#add comment view for a seperate page
def addcomment(request):
    request.method = 'POST'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = form.save()
            return HttpResponseRedirect('/index')
    else:
        return form

#addpost view for a seperate page
def addpost(request):
    request.method = 'POST'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newpost = form.save()
            return HttpResponseRedirect('/index')
    else:
        form = CommentForm()
    return render(request, 'codhc/add.html', {'form':form})