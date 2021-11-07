
from django import forms
import django
from django.http import request

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.
def skill (request):
    context={'skill':'active'}
    return render(request, "edu/skill.html", context)
def login (request):
    context={'login':'active'}
    return render(request, "edu/login.html", context)
def thankyou(request):
    return render(request, 'edu/success.html' )
def showformdata(request):
    if request.method == "POST" :
     fm = StudentRegistration(request.POST )
     if fm.is_valid():
         name = fm.cleaned_data['name']
         email = fm.cleaned_data['email']
         password= fm.cleaned_data['password']
         
         return HttpResponseRedirect('/regi/success/' )
        
    else:
        fm = StudentRegistration()
     
    return render(request, 'edu/login.html', {'form':fm})



