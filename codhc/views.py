from django.shortcuts import render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Post, Comment
from .forms import NameForm
# Create your views here.

def index(request):
    latest_post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'codhc/index.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id, pub_date__lte=timezone.now())
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'codhc/detail.html', {'post': post})


def get_queryset(self):
    """
    Populate the dashboard with the last 10 posts
    """
    return Post.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:10]