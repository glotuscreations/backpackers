from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import View
from . import models


# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request,"blog/home.html", {'posts': posts})

def post_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request,"blog/about.html", {'about':about})
