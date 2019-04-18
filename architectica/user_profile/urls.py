from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

app_name="user_profile"
urlpatterns = [
  path('view_profile/<int:id>',view_profile,name='view_profile' ),
  path('dashboard',dashboard,name='dashboard' ),
  path('reviews',reviews,name='reviews' ),
  path('settings/<int:id>',setting,name='setting' ),
  path('wishlist',wishlist,name='wishlist' )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)