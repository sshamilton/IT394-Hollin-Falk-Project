from django.shortcuts import render
from django.template import loader
from .models import Cadet
from .models import Company
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CadetForm
from .forms import CompanyForm

# Create your views here.
def index(request):
    users = User.objects.all() #all django registered users
    context = {'users': users} #fill a context with the cadet list
    template = loader.get_template('users/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def detail(request, cadet_id):
    try:
        cadet = Cadet.objects.get(pk=cadet_id)
        companies = Company.objects.all()
        context = {'cadet':cadet, 'companies': companies}
    except Cadet.DoesNotExist:
        raise Http404("Cadet does not exist")
    return render(request, 'users/detail.html', context)

def update(request, cadet_id):
    new_xnumber = request.POST['xnumber']
    new_company_id = request.POST['company_id']
    cadet = Cadet.objects.get(pk=cadet_id)
    cadet.xnumber = new_xnumber
    cadet.company_id = new_company_id
    cadet.save()
    companies = Company.objects.all()
    context = {'cadet':cadet, 'companies': companies}
    return render(request, 'users/detail.html', context)

def addcadet(request):
    if request.method == 'POST':
        form = CadetForm(request.POST)
        if form.is_valid():
            #Add the cadet to the database
            newcadet = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/index')
        else:
            form = CadetForm()
            return render(request, 'users/add.html', {'form': form})
    else:
        return (HttpResponse("You are not allowed to add cadets"))

        
def addcompany(request):
    #if user.has_perm('cadet.add_cadet'):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            #Add the company to the database
            newcompany = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/users')
    else:
        form = CompanyForm()
    return render(request, 'users/addcompany.html', {'form': form})

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
