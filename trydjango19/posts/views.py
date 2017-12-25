from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title" : 'list',
        'object_list' : queryset
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")