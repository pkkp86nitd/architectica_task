from django.db import models
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def content_file_name(instance,filename):
	ext="png"
	filename= str(instance.name)+"."+str(ext)
	return os.path.join('images/',filename)
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    role_choices = (
        ('1', 'customer'),
        ('2', 'partner'),
        ('3', 'sponsor')
    )
    role = models.CharField(max_length=50, choices=role_choices ,default='1')
    occupation = models.CharField(max_length=20, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to=content_file_name)
    email_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self,  *args, **kwargs):
        if self.image:
          img= Image.open(self.image)
          output = BytesIO()
          img = img.resize((100, 100))
          img.save(output, format='PNG', quality=100)
          output.seek(0)
          self.image = InMemoryUploadedFile(output, 'ImageField', ".png" , 'image/png',
                                        sys.getsizeof(output), None)
        super(Profile, self).save()    
    class Meta:
        managed = True