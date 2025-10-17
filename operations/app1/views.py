from django.shortcuts import render

# Create your views here.
import math
def addition(request):
    if (request.method=="POST"):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)

    if (request.method=="GET"):
        return render(request, 'addition.html')

def fact(request):
    if request.method=='POST':
        n=int(request.POST['n'])
        f=math.factorial(n)
        context={'fact':f}
        return render(request,'signup.html',context)

    if (request.method=="GET"):
        return render(request, 'signup.html')

def bmi(request):
    if request.method=='POST':
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])
        b=n1/n2**2
        context={'bmi':b}
        return render(request,'bmi.html',context)

    if (request.method=="GET"):
        return render(request, 'bmi.html')
