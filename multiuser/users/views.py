from django.shortcuts import render, redirect
from users.forms import Signupform
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
# Create your views here.
from django.views import View

from users.forms import Loginform


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class Register(View):
    def post(self,request):
        form_instance = Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            messages.error(request,'ERROR')
            return render(request, 'login.html', {'form': form_instance})
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request, 'register.html',context)



class Userlogin(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request, 'login.html',context)
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user and user.role=='student':
                login(request, user)
                return redirect('studenthome')
            elif user and user.role=='teacher':
                login(request, user)
                return redirect('teacherhome')
            else:
                messages.error(request,'INVALID CREDENTIALS')
                return redirect(request.path)

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

