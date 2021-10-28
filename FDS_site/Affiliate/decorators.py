from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page")
        return wrapper_func
    return decorators


def Affioiate_admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Affiliate_admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func