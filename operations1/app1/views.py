from django.shortcuts import render

from app1.forms import AdditionForm
from app1.forms import BMIForm
from app1.forms import Signup
from app1.forms import Diet


# Create your views here.

def addition(request):
    if (request.method=='POST'):
        print(request.POST)
        #creating form_instance using submitted data
        form_instance=AdditionForm(request.POST)
        #check whether the data is valid
        if form_instance.is_valid():
            #process data
            data=form_instance.cleaned_data
            print(data)
            n1=int(data['num1'])
            n2=int(data['num2'])
            s=n1+n2
            context={'result':s,'form':form_instance}
        return render(request, 'addition.html',context)

    if (request.method=='GET'):
        form_instance=AdditionForm()
        context={'form':form_instance}
        return render(request,'addition.html',context)

def bmi(request):
    if request.method=='POST':
        form_instance=BMIForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            n1=float(data['weight'])
            n2=float(data['height'])
            r=n1/n2**2
            context={'bmi':r,'form':form_instance}
            return render(request,'bmi.html',context)
    if (request.method == 'GET'):
        form_instance = BMIForm()
        context = {'form': form_instance}
        return render(request, 'bmi.html', context)


def signup(request):
    if request.method=='POST':
        form_instance=Signup(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            pl=data['place']
            ge=data['gender']
            r=data['role']
            e=data['email']
            context={'username':u,'password':p,'place':pl,'gender':ge,'role':r,'email':e,'form':form_instance}
            return render(request,'signup.html',context)

    if request.method=='GET':
        form_instance=Signup()
        context={'form':form_instance}
        return render(request,'signup.html',context)


def diet(request):
    if request.method=='POST':
        form_instance=Diet(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            g=data['gender']
            w=data['weight']
            h=data['height']
            a=data['age']
            al=float(data['activity_level'])

            if g=='male':
                BMR= 10 * w + 6.25 * h -5 * a + 5
            else:
                BMR= 10 * w + 6.25 * h - 5 * a - 161
            c=int(BMR*al)
            context={'result':c,'form':form_instance}
            return render(request, 'diet.html',context)

    if request.method == 'GET':
        form_instance = Diet()
        context = {'form': form_instance}
        return render(request, 'diet.html', context)
