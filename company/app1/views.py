from django.shortcuts import render, redirect
from app1.forms import Employeeform
from app1.models import Employee

# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request,'home.html')

def addemp(request):
    if request.method=="POST":
        form_instance=Employeeform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:viewemploye')
    if request.method=="GET":
        form_instance=Employeeform()
        return render(request,'addemploye.html',{'form':form_instance})

def viewemp(request):
    e=Employee.objects.all()
    context={'emp':e}
    return render(request,'viewemploye.html',context)