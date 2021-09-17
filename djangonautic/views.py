from django.http import HttpResponse
from django.shortcuts import render # render renders templates

def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'homepage.html') # render(request, html file)

def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')