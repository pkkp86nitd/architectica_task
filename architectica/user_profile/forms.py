from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import mimetypes
from .validators import *
from django.contrib.auth.forms import UserCreationForm

class Profileform(forms.ModelForm):
    name = models.CharField(max_length=100)
    country = models.TextField(max_length=100)
    occupation = models.IntegerField()

    def clean_image_url(self):
        url = self.cleaned_data['image_url'].lower()
        if not valid_url_extension(url) or not valid_url_mimetype(url):
            raise forms.ValidationError(_("Not a valid Image. The URL must have an image extensions (.jpg/.jpeg/.png)"))
        return url

    class Meta:
        model = Profile
        fields = ('name', 'country', 'occupation', 'image',)