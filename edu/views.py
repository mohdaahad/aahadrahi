
from django import forms
import django
from django.http import request

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

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
         print('Name', name )
         print('email', email)
         print('password', password)
         return HttpResponseRedirect('/regi/success/' )
        #  return render(request, 'edu/success.html', {'nm':name})
    else:
        fm = StudentRegistration()
    # for field in fm:
    #     print("%%%%%%%%%%:::: ",field,field.widget_type)    
    return render(request, 'edu/login.html', {'form':fm})



