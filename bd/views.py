from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bangladesh
from django.contrib import messages
import re

from .models import Sodesh

from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/sodeshDat')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

# Create your views here.


def bangladesh(request):
    bangladeshData = serialize('geojson', Bangladesh.objects.all())
    return HttpResponse(bangladeshData, content_type='geojson')

def sodesh(request):
    sodeshData = serialize('geojson', Sodesh.objects.all())
    return HttpResponse(sodeshData, content_type='geojson')


def more_information(request):
    sodeshData =  Sodesh.objects.all()
    fg = str(request.get_full_path)
    
    ft1 = str(re.findall("[0-9]", fg))
    ft2 = str(re.findall("[0-9][0-9]", fg))
    ft3 = str(re.findall("[0-9][0-9][0-9]", fg))
    x1 = '\n'.join(ft1)
    x2 = '\n'.join(ft2)
    x3 = '\n'.join(ft3)


    d1 = x1[4:5]
    d2_1 = x2[4:5]
    d2_2 = x2[6:7]
    d2 = d2_1 + d2_2
    d3_1 = x3[4:5]
    d3_2 = x3[6:7]
    d3_3 = x3[8:9]   
    d3 = d3_1 + d3_2 +d3_3

    if len(d3) > 2:
        sum = d3
    elif len(d2) > 1:
        sum = d2
    else:
        sum = d1


    

    return render(request, 'more_information.html', locals())



def more_informationht(request):
    return render(request, 'more_information.html')

def index(request):
    return render(request, 'index.html')


def home(request):

    return render(request, 'public_data.html')

def  about_pims(request):
    return render(request,'about_PIMS.html')




def  contact(request):
    return render(request,'contact_us.html')
def pricing(request):

    return render(request, 'pricing.html')

def homeso(request):

    return render(request, 'home_sodesh.html')



