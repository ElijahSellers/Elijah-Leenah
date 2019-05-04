from django.urls import path, include, re_path

from django.conf.urls import url
from .models import Post
from .forms import *
from . import views

urlpatterns= [
    path('',views.home, name='home'),
    path('About_us/',views.about, name="About Us"),
    path('Gallery/',views.gallery, name="Gallery"),
    re_path(r'^(?P<pk>[0-9]+)/delete_answer/$', views.objectDelete, name='delete_object'),
]
