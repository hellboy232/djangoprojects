from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def First(request):
#     return HttpResponse("first page")
#
# def Second(request):
#     return HttpResponse("second page")

def first(request):
    context={'name':'hrithik','age':21}
    return render(request,'first.html',context) #context-is a dictionary type
                                                            # is used to pass data from views to html page

def second(request):
    context={'name':'arun','age':20}
    return render(request,'second.html',context)