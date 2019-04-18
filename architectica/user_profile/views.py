from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.models import *

# Create your views here.
def view_profile(request, id=None):
    try:
        profile = get_object_or_404(Profile, pk=id)
    except:
        return HttpResponse("User has not created a Profile yet!")
    args = {'profile': profile,  }
    return render(request, 'profile/profile.html', args)

def dashboard(request,):
    return render(request, 'dashboard.html')
def reviews(request,):
    return render(request, 'reviews.html')
def wishlist(request,):
    return render(request, 'wishlist.html')
def setting(request,):
    return render(request, 'settings.html')    
    
    