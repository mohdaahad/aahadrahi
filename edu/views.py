from django.http import request
from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm = StudentRegistration(label_suffix="")
    # print("**********************",fm.as_p() , type(fm))
    return render(request, 'edu/userregistration.html', {'form':fm })
