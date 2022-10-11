from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render

from blog.models import Post,Category

# Create your views here.

def get_all_blogs(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return JsonResponse(posts[0].title)

def get_blog_with_id(request,id):
    if request.method == "GET":
        post = Post.objects.get(pk=id)
        data = {}
        data = model_to_dict(post)
        return JsonResponse(data)
