from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpResponse
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='re'),
]
