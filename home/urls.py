from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.landing_page,name='landing'),
    path('home',views.home_page,name='home'),
    path("register", views.landing_page_register, name="reg")
]