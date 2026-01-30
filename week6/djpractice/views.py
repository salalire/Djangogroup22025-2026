from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post

def sayhello(request):
    return HttpResponse('Hello Blog')

class CBF(View):
    def get(self, request):
        return HttpResponse("Welcome To Django CBV")
def fetch_posts(request):    
    posts=Post.objects.all()
    titles=[]
    for p in posts:
        titles.append(p.title)
    if not titles:
        return HttpResponse("No posts available")
    else:
        return HttpResponse(', '.join(titles))    

