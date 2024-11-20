from django.shortcuts import render, HttpResponse

def home(request):
    #return render(request, "core/base.html")
    return HttpResponse("<h1>Desafio de codificação - AG Sistemas</h1>")

def viewBlog(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'core/blog.html', {'posts': posts, 'tags': tags})
