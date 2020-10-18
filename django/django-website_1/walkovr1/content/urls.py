from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "content"

urlpatterns = [    
    path('dashboard/',views.panel, name = "panel"), #/panelapp/views yoluyla panel.html
    path('addcontent/', views.addContent, name= "addcontent"),
    path('adminpanel/', views.adminpanel, name= "adminpanel"),
    #path('commercialpanel/', views.commercialpanel, name= "commercialpanel"),
    path('commercialpanel/<int:id>', views.userdetail_atcommercial, name= "userdetail_atcommercial"),
    path('adminpanel/<int:id>', views.userdetail_atadmin, name= "userdetail_atadmin"), #id gelecek ve biz bunu int şeklinde alacağız
    #path('commercialpanel/', views.commercialpanel, name= "cpanel"),
    #path('commercialpanel/<int:id>', views.userdetail, name= "cuserdetail"), #id gelecek ve biz bunu int şeklinde alacağız
    path('addtogroup/', views.addtoGroup, name= "addtogroup"),
    path('removefromgroup/', views.removefromGroup, name= "removefromgroup"),
    path('contentt/', views.ContentAPI.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)