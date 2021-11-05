from django.shortcuts import render
from .forms import StudentRegistration
def showformdata(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
       print('from validated') 
       print('Name:', fm.cleaned_data['name'])
       print('Email:',fm.cleaned_data['email'])
    else:
      fm = StudentRegistration()   

    return render(request, 'edu/userregistration.html',{'form':fm})

