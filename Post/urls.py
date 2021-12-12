from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage ,name="main"),
    
     path('about',views.aboutpage ,name="about"),
      path('contact',views.contactpage ,name="contact"),
      
      path('home',views.dashboardpage ,name="home"),
]