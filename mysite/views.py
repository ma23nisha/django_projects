from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>Hello</h1>")

def removepunc(request):
    text = request.GET.get('text','default')
    print(text)
    return HttpResponse("capitalize first")

def capfirst(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("space remove")