from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy


class LoginYSuperUsuarioMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser: 
                return super().dispatch(request, *args, **kwargs)
            messages.error(request, 'Lo siento! no tienes permiso para realizar esta acción.')
        return redirect('home_app:index')
    
class ValidarPermisosRequeridosMixin(object):
    permission_required = ''
    url_redirect = None
    
    def get_perms(self):
        if isinstance(self.permission_required, str): 
            return (self.permission_required)
        else:
            self.permission_required
            
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('users_app:user-login')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'Lo siento! no tienes permiso para realizar esta acción.')
        return redirect(self.get_url_redirect())
    
    