from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>Hello</h1>")

def analyze(request):
    text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(text)
    if removepunc=="on":
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in text:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    else:
        return HttpResponse("Error")
        
    return render(request,'analyze.html',params)


def removepunc(request):
    text = request.GET.get('text','default')
    removepunc = request.GET.get('text','off')
    print(removepunc)
    print(text)
    return HttpResponse("capitalize first")

def capfirst(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("space remove")