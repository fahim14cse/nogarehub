from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    path('', views.deshboard, name='Deshboard') ,   
    path('home/', views.home, name='Home') ,
    path('blog/', views.blog, name='Blog') ,
    path('about/', views.about, name='About') ,
    path('contract/', views.contract, name='contract'),
    path('show_data/', ShowData.as_view(), name='show-data') ,  
 
]
