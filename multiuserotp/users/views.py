from django.shortcuts import render, redirect
from users.forms import Signupform
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.core.mail import send_mail
from django.views import View

from users.forms import Loginform

from users.models import CustomUser


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
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "OTP for sign in:",u.otp,
                "glooexpress25@gmail.com",[u.email],
                fail_silently=False,
                        )
            return redirect('otp_verification')
        else:
            messages.error(request,'ERROR')
            return render(request, 'login.html', {'form': form_instance})
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request, 'register.html',context)

class Otp_verification(View):
    def get(self,request):
        return render(request,'otp_verification.html')

    def post(self,request):
        try:
            o=request.POST['o']
            u=CustomUser.objects.get(otp=o)
            u.is_verfied=True
            u.is_active=True
            u.save()
            return redirect('login')
        except:
            messages.error(request,'INVALID OTP')
            return redirect(request.path)

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

