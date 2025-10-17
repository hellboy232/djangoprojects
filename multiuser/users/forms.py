from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import CustomUser



class Signupform(UserCreationForm):
    role_choice = (('student', 'Student'), ('teacher', 'Teacher'))
    role = forms.ChoiceField(choices=role_choice)
    gender_choice = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect)
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone','role','gender']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)