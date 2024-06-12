from django.http import HttpResponse
from django.shortcuts import redirect

# verificar se o usuario esta logado, se estiver, nega acesso a view
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('academia:index')
        else:
            return view_func(request,*args, **kwargs)
    
    return wrapper_func

# verificar a permiçao do usuario
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('login')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
        return HttpResponse("Somente administradores têm acesso.", status=403)
        
    return wrapper_function