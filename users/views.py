from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    users = User.objects.all() #all django registered users
    context = {'users': users} #fill a context with the cadet list
    template = loader.get_template('users/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def adduser(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/users')
    return render(request, 'users/add.html', {'form': form})
