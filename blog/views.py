from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'blog/home.html')
    #return HttpResponse('<h1>helooo</h1>')

def about(request):
    return render(request,'blog/about.html')
    #return HttpResponse('<h1>about page here!</h1>')