from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post,Category
from blog.serializers import PostSerializer

# Create your views here.

@api_view(['GET'])
def get_all_blogs(request):
    if request.method == "GET":
        posts = Post.objects.all()
        data = []
        if posts:
            for i in posts:
                data.append(PostSerializer(i).data)
                # data.append(model_to_dict(i,fields=['id','title','body','created_on','new_title']))
        return Response(data=data)
        # return JsonResponse({"message":data},safe=False)

@api_view(['GET'])
def get_blog_with_id(request,id):
    if request.method == "GET":
        post = Post.objects.get(pk=id)
        data = {}
        data = model_to_dict(post,fields=['id','title','body'])
        return Response(data=data)
        # return JsonResponse({"message":data},safe=False)
