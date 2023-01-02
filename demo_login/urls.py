
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'demo_login'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.usersignup,name='signup'),
    path('logout/',views.userlogout,name='logout'),
    path('login/',views.userlogin,name='login'),
    path('add/',views.add,name='add'),
    path('specificsupdate/<int:id>',views.update,name='update'),
    path('specificsdelete/<int:id>',views.delete,name='delete'),
    path('modal/',views.modal,name='modal'),
]
