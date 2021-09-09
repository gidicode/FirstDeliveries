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

            if group == 'Fleet Manager':
                return redirect('/')

            if group == 'Cashier':
                return redirect('/')

            if group == 'Front Desk':
                return redirect('/')

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        
    return wrapper_func

def flls_team(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('/')

            if group == 'Fleet Manager':
                return redirect('/')

            if group == 'Cashier':
                return redirect('/')

            if group == 'Front Desk':
                return redirect('/')

            if group == 'FLLS':
                return view_func(request, *args, **kwargs)                    
    return wrapper_func