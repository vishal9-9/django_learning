from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from polls.models import Project

# Create your views here.


def index(request):
    return HttpResponse("Hello World, from polls app.")

@csrf_exempt
def detail(request,id):
    if request.method == "GET":
        return HttpResponse(f"Hello World, from polls app with id :- {id}")
    elif request.method == "POST":
        return HttpResponse(f"Hello World, from polls app with id :- {id}")

def project_details(request,id):
    if request.method == "GET":
        data = Project.objects.get(pk=id)
        # context = {
        # "project": data,
        # }
        # return render(request, "blog_index.html", context)
        return HttpResponse(f"Data :- {data.description}")

def project_details_all(request):
    if request.method == "GET":
        data = Project.objects.all()
        return HttpResponse(data[1].description)
