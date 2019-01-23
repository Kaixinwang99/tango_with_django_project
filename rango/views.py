from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #Rango says hey there partner! <br/><a href='/rango/about/'>About</a>
    return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>About</a>")

def about(request):
    #<a href="/rango/">Index</a>
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
