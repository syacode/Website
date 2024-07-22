from django.http import HttpResponse
from django.shortcuts import redirect ,render

def unauthenticate_user (view_func):
    def wrapper_func(request , *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home') #render(request, 'MyC/Home.html')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request , *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("TIADA AKSES KEPADA MAKLUMAT")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'user':
            return redirect('register')#render(request, 'MyC/Register.html')
        
        if group == 'JKDM_user':
            return redirect('JKDM_user') #render(request, 'MyC/Home.html')
        
        if group == 'JKDM_admin':
            return redirect('JKDM_admin') #render(request, 'MyC/Home.html')
        
        if group == 'admin' :
            return view_func(request,*args,**kwargs)
        
    return wrapper_function