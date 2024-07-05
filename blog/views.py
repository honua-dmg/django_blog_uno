from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
posts = [
    {
        'author': 'Guru Sai',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Suru Gai',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')
    #return HttpResponse('<h1>about page here!</h1>')