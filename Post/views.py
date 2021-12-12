from django.shortcuts import render

# Create your views here.

def homepage(request):
    context={}
    
    return render(request,'layouts/home.html',context)

def contactpage(request):
    context={}
    
    return render(request,'layouts/contact.html',context)


def aboutpage(request):
    context={}
    
    return render(request,'layouts/about.html',context) 

def dashboardpage(request):
    
    context={}
    
    return render(request,'layouts/dashboard.html',context)
