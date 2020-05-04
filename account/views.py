from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy, reverse
from django.views import generic 
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

class SignUp(generic.CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
def index(request):
    return render(request, 'account/login.html')