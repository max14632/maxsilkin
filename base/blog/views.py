from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #"folder" with all of the posts



# Create your views here.


def home(request):
    return render(request, 'blog/portfolio.html')


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)
