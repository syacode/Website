"""
URL configuration for Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from MyC import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls, name= 'admin'),
    path('register/', views.register, name='register'),
    path('home/', views.home , name='home' ),
    path('auth', include('django.contrib.auth.urls') ),
    path('', views.login_user,name='login' ),
    path('logout_view/', views.logout_view,  ),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('JKDM_admin/', views.JKDM_admin, name='JKDM_admin'),
    path('JKDM_user/', views.JKDM_user, name='JKDM_user'),
    path('register_user/', views.Register_user, name='register_user'),
]
