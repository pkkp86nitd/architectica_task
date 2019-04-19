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
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from itertools import chain
from django.core.files.base import ContentFile
from io import BytesIO
import urllib.request
from PIL import Image
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import *
import random

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
def setting(request,id):
    try:
        profile=get_object_or_404(Profile,pk=id)
    except:
        return HttpResponse("no PRofile if this id")    
   
    form = Profileform(request.POST or None, request.FILES or None,  instance=profile)
    if form.is_valid():
        form.save()
        print(form.cleaned_data['image'])
        if form.cleaned_data['image'] is None or form.cleaned_data['image'] == False or not (form.cleaned_data['image']):
          image_url = "https://api.adorable.io/avatars/"+ str(random.randint(0000,9999))
          type = valid_url_extension(image_url)
          full_path = 'media/images/' + profile.name + '.png'
          try:
              urllib.request.urlretrieve(image_url, full_path)
          except:
              return HttpResponse("Downloadable Image Not Found!")
          
          profile.image = '../' + full_path
          form.save()
        return HttpResponseRedirect(reverse('user_profile:view_profile', args=(id,)))
    form=Profileform(instance=profile)        
    return render(request, 'settings.html',{'form':form})    
    
    