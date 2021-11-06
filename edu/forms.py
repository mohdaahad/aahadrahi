from django.core import validators
from django import forms
from django.forms import widgets

class StudentRegistration(forms.Form ):
    def starts_with_s(value):
      if value[0] != 's':
        raise forms.ValidationError('Name should start with s')
    name=forms.CharField( label_suffix="",widget=forms.TextInput(attrs={'placeholder':'Username'}),label="" ) 
    email=forms.EmailField(label_suffix="",widget=forms.TextInput(attrs={'placeholder':'Email'}),label="")
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label_suffix="", label="" )
    agree= forms.BooleanField()
