from tkinter import Widget
from turtle import width
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    emp_id = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'emp_id', 'first_name', 'last_name', 'email', 'password1', 'password2']

class EmployeeForm(ModelForm):
    department_choice = [
        ('Python','Python'),
        ('Django ','Django '),
        ('Java Script','Java Script'),
        ('Angular','Angular'),
        ('React','React'),
    ]
    role_choice = [
        ('HR','HR'),
        ('Marketing','Marketing'),
        ('Tester','Tester'),
        ('JR. Developer','JR. Developer'),
        ('SR. Developer','SR. Developer'),
    ]
    department = forms.ChoiceField(widget=forms.RadioSelect,choices=department_choice)
    role = forms.ChoiceField(choices=role_choice)
    class Meta:
        model = Employee
        fields = ['first_name','last_name','employee_id','department','role',
        'salary','bonus','phone_number','email_id']