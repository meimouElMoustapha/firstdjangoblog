from django.urls import path
from . import views
from django.contrib.auth import logout
from .views import ArticleListView,detailpage,createpost1 #,UpdateView
# from .views import ArticleListView

urlpatterns = [
    path('logout',logout,name="logout"),
    path('',views.homepage ,name="main"),
    path('home',ArticleListView.as_view() ,name="home"),
    path('create',views.createpost1 ,name="create"),
    path('<pk>/',detailpage.as_view(template_name='layouts/detail.html' ) ,name="detail"),
    
    
    # path('<pk>/update', UpdateView.as_view(template_name='layouts/edit.html'  ),name="update"), 
    path('about',views.aboutpage ,name="about"),
    path('contact',views.contact_info ,name="contact"),
    #   path('list', ArticleListView.as_view(), name='article-list'),
    # path('home',views.dashboardpage ,name="home"),
]