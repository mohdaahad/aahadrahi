from django.urls import path 
from . import views
urlpatterns = [
   
    path ("registration/", views.showformdata ,name="regis"),
    path ("success/", views.thankyou ),
   
]


