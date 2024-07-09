from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
import tkinter as tk
from tkinter import messagebox
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorator import unauthenticate_user , allowed_users , admin_only
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#Login_method here
@unauthenticate_user
def login_user(request):
    request.session.flush()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #URl to home
            return redirect('home')
        else:
             # Return an 'invalid login' error message.
            messages.success(request,("Kesilapan maklumat akaun dikunci masuk"))
            return redirect('login')#render(request, 'MyC/Login.html')
    else:
        return render(request, 'MyC/Login.html')

#Homepage
@login_required(login_url='login')
@admin_only#Decarotor
def home(request):

    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # Add any other user-related information you need
    }

    return   render(request, 'MyC/Home.html')

#register
@login_required
def register(request):
    return render (request, 'MyC/Register.html')


def logout_view(request):
    return  redirect (logout)#render (request, 'MyC/logout.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Clear the session
        request.session.flush()
        return super().dispatch(request, *args, **kwargs)
    
 #jkdm page admin   
@login_required    
def JKDM_admin(request):
    return render(request, 'MyC/JKDM_admin.html')

 #jkdm page user   
@login_required
def JKDM_user(request):
    return render(request, 'MyC/JKDM_user.html')

#User Registration

def Register_user(request):
    form = UserCreationForm()
    context = {'form':form}

    return render(request, 'Myc/Register_user.html',context)