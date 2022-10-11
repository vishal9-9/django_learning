from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post,Category

# Create your views here.

def get_all_blogs(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return HttpResponse(posts[0].title)

def get_blog_with_id(request,id):
    if request.method == "GET":
        posts = Post.objects.get(pk=id)
        return HttpResponse(posts.body)
