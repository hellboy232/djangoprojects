from django import forms
from django.forms import RadioSelect


class AdditionForm(forms.Form):

    num1=forms.IntegerField()
    num2=forms.IntegerField()

class BMIForm(forms.Form):
    weight=forms.FloatField()
    height=forms.FloatField()

class Signup(forms.Form):

    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('admin','Admin'),('student','Student'))

    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    place=forms.CharField()
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    email=forms.EmailField()

class Diet(forms.Form):
    gender_choices = (('male', 'Male'), ('female', 'Female'))
    activity_choices=(('1.2','sedentary'),('1.375','lightly active'),('1.55','moderately active '),('1.725','very active'),('1.9',' extra active'))

    gender=forms.ChoiceField(choices=gender_choices,widget=RadioSelect)
    weight=forms.IntegerField()
    height=forms.IntegerField()
    age=forms.IntegerField()
    activity_level=forms.ChoiceField(choices=activity_choices)


