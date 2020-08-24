from django.shortcuts import render
from .models import Post


# Create your views here.

def home(Request):
    context = {
        'posts': Post.objects.all()
    }
    return render(Request, 'blog/home.html', context)


def about(Request):
    return render(Request, 'blog/about.html', {'title': 'About'})
