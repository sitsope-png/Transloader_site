
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [

path('inscription/', views.inscription, name='inscription'),
path('acces/', views.acces, name='acces'),
]