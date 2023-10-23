from django.shortcuts import render
from django.http import HttpResponse
from .models import  Post


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')




def about(request):
    blog_post = Post.objects.all()
    return render(request, 'blog/about.html',{"blog_post": blog_post})
