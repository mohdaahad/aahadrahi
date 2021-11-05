from django import forms
from django.forms import widgets

class StudentRegistration(forms.Form ):
    name=forms.CharField()
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

