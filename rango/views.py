from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page. <br /><a href='/rango/'>Index</a>")
