from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
        
def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not Authorized to view this Page')
        return wrapper_func
    return decorators

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('/')

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        
    return wrapper_func

def fleet_manager_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('/')

            if group == 'Front Desk':
                return HttpResponse('You are not Authorize to view this Page')

            if group == 'Front Desk':
                return HttpResponse('You are not Authorize to view this Page')

            if group == 'Cashier':
                return HttpResponse('You are not Authorize to view this Page')
            
            if group == 'Fleet Manager':
                return view_func(request, *args, **kwargs)

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        
    return wrapper_func


def front_desk_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('/')

            if group == 'Cashier':
                return HttpResponse('You are not Authorize to view this Page')
            
            if group == 'Fleet Manager':
                return HttpResponse('You are not Authorize to view this Page')
            
            if group == 'Front Desk':
                return view_func(request, *args, **kwargs)

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        
    return wrapper_func


def Cashier_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('/')
    
            if group == 'Fleet Manager':
                return HttpResponse('You are not Authorize to view this Page')
            
            if group == 'Front Desk':
                return HttpResponse('You are not Authorize to view this Page')

            if group == 'Cashier':
                return view_func(request, *args, **kwargs)

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        
    return wrapper_func