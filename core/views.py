from django.shortcuts import render, HttpResponse
from .models import Post, Tag

def home(request):
    return render(request, "core/home.html")
    #return HttpResponse("<h1>Desafio de codificação - AG Sistemas</h1>")

def viewBlog(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, "core/blog.html", {'posts':posts, 'tags':tags})
