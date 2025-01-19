from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.index , name='home'),
    path("about" , views.about , name='about'),
    path("services" , views.services , name='services'),
    path("contect" , views.contect , name='contect'),
    path("show" , views.show , name='show'),
    path("delete/<id>/" , views.delete , name='delete'),
    path("edit/<id>/" , views.edit , name='edit'),

    

]