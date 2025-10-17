
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from users.forms import Signupform
from users.forms import Loginform


class Register(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html',context)

class Login(View):
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request, user)
                return redirect('books:home')
            else:
                messages.error(request,'Invalid Credentials')
                # Redirect to same page without re-rendering POST response
                return redirect(request.path)


    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')


