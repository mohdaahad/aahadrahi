from django.core import validators
from django import forms
from django.forms import widgets

class StudentRegistration(forms.Form ):
    def starts_with_s(value):
      if value[0] != 's':
        raise forms.ValidationError('Name should start with s')
    name=forms.CharField() 
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

