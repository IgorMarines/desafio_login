from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.index, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]
