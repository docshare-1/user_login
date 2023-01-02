from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'todouser'
urlpatterns = [
   path('',views.userLogin,name='login'),
   path('logout/',views.userLogout,name='logout'),
   path('signup/',views.userSignup,name='signup'),
   path('index/',views.index,name='index')
]
