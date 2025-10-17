from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

