from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    removespace = request.POST.get('removespace','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == "on":
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
       

    if(fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Upper','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    

    if(removespace == "on"):
        analyzed = ""
        for char  in text:
            if char!=" ":
                analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Upper','analyzed_text':analyzed}
        return render(request,'analyze.html',params)


    if(charcount == "on"):
        count = 0
        for char in text:
            count += 1
        params = {'purpose':'character count','analyzed_text':count}
        return render(request,'analyze.html',params)
            
    if(newlineremove == "on"):
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed = analyzed + char.upper()
        params = {'purpose':'remove newline','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")
        
   


def removepunc(request):
    text = request.POST.post('text','default')
    removepunc = request.POST.post('text','off')
    print(removepunc)
    print(text)
    return HttpResponse("capitalize first")

def capfirst(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("space remove")