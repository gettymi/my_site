from django.shortcuts import render
from django.http import Http404
from .models import Post
# Create your views here.




def index_page(request):
    posts = Post.objects.all()
    latest_posts = posts.order_by('-date')[:3]
    return render(request,"blog/index.html", {"posts" : latest_posts})

def all_posts(request):
    posts = Post.objects.all()
    return render(request,"blog/all_posts.html",{"posts": posts})

def post_detail(request,slug):
    posts = Post.objects.all()
    for post in posts:
        if post.slug== slug :
            tag = post.tag.all()
            return render(request,"blog/post_detail.html",{"post":post,"tags":tag})

    return Http404()