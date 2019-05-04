from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from leblog.models import Post
from leblog.forms import PostArticle
from django.views import View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

import json

from django.contrib.messages.views import SuccessMessageMixin

from .forms import *

from .models import *
# Create your views here.
def home(request):

    if request.method == "POST":
        form = PostArticle(request.POST)
        if form.is_valid():
            form = form.save()
            redirect('/')
    else:
        form = PostArticle()
    Display_Posts = Post.objects.all().order_by('-publish_date')
    context = {'Display_Posts':Display_Posts,
               'form':form}


    return render(request, 'leblog/Home.html', context)

def about(request):
    return render(request, 'leblog/About_us.html')


def gallery(request):
    return render(request, 'leblog/Gallery.html')

def contact(request):
    return render(request, 'leblog/Contact_Us.html')

def objectDelete(DeleteView, object_id):
    object = get_object_or_404(Model, pk=object_id)
    object.delete()
