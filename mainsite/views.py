from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime


# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        now = datetime.now()
        if slug != None:
            return render(request, 'blog-single.html', locals())
    except:
        return redirect('/')


def blog(request):
    return render(request, 'blog.html')


def page_not_found(request):
    return render(request, '404.html')
