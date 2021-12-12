from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


# Create your views here.
from django.utils import timezone
from .forms import contact,createpost
from .models import Post
from django.contrib import messages


# class UpdateView(UpdateView):
#     # specify the model you want to use
#     model = Post
#     form=Post.objects.all()
    
#     success_url ="/home"

def contact_info(request):
    form = contact(request.POST or None)
    if form.is_valid():
        form.save()
        form=contact()
        messages.add_message(request, messages.INFO, 'message sent successfully!')
    context={'form':form}
    
    return render(request,"layouts/contact.html",context)


def createpost1(request):
    form = createpost(request.POST or None)
    if form.is_valid():
        form.save()
        form=createpost()
        messages.add_message(request, messages.INFO, 'post created successfully!')
    context={'form':form}
    
    return render(request,"layouts/createPost.html",context)






class ArticleListView(ListView):
    
    model=Post
    
    # def get_context_data(self,pk, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['features'] = Post.objects.get(id=pk)
    
    
    def get(self,request,*args, **kwargs):
        featured=Post.objects.all()
        most_recent=Post.objects.order_by('author')[0:3]
        
        context={'features':featured,'most_recent':most_recent}
        
        return render(request,'layouts/list.html',context)


class detailpage(DetailView):
    # specify the model to use
    model = Post
    post=Post.objects.all()
   
   
def homepage(request):
    context={}
    
    return render(request,'layouts/home.html',context)




def aboutpage(request):
    context={}
    
    return render(request,'layouts/about.html',context) 

# def dashboardpage(request):
    
#     context={}
    
#     return render(request,'layouts/dashboard.html',context)
