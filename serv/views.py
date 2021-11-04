from django.shortcuts import render


def services(request):
 context={'services':'active'}
   
 return render(request, "serv/services.html", context)