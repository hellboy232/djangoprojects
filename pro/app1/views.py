from django.http import HttpResponse
from django.shortcuts import render

#Function Based View
# def functionname(parameter):
#       pass

def Home(request):
    return HttpResponse("Welcome to new Django App")

def Index(request):
    return HttpResponse("welcome to index page")