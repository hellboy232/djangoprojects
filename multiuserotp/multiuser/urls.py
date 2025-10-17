"""
URL configuration for multiuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('adminhome',views.Adminhome.as_view(),name='adminhome'),
    path('teacherhome',views.Teacherhome.as_view(),name='teacherhome'),
    path('studenthome',views.Studenthome.as_view(),name='studenthome'),
    path('register',views.Register.as_view(),name='register'),
    path('login',views.Userlogin.as_view(),name='login'),
    path('logout',views.Userlogout.as_view(),name='logout'),
    path('otp_verification',views.Otp_verification.as_view(),name='otp_verification'),

]
