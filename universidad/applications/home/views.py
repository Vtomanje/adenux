import time
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from applications.home.models import Banner


# Create your views here.

def plural_to_singular(plural):
        # Diccionario de palabras
    plural_singular = {
        "estudiantes": "estudiante",
        "profesores": "profesor",
        "evaluaciones": "evaluacion",
        "administradores": "administrador",
    }
    
    return plural_singular.get(plural, "Esta palabra no existe")

def add_group_name_to_context(view_class):
    original_dispatch = view_class.dispatch 
    
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        group = user.groups.first()
        group_name = None
        group_name_singular = None
        color = None
        if group:
            if group.name == 'estudiantes':
                color = 'bg-blue-800'
            elif group.name == 'profesores':
                color = 'bg-green-500 text-white'
            elif group.name == 'evaluaciones':
                color = 'bg-red-800'
            elif group.name == 'administradores':
                color = 'bg-pink-600 text-white'
                
            group_name = group.name
            group_name_singular = plural_to_singular(group.name)
        
        context = {
            'group_name': group_name,
            'group_name_singular': group_name_singular,
            'color': color
        }
        
        self.extra_context = context
        return original_dispatch(self, request, *args, **kwargs)
    
    view_class.dispatch = dispatch
    return view_class
     
@add_group_name_to_context       
class CustomTemplateView(TemplateView):
    group_name = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name
        context ['group_name'] = group_name
        return context
    
@add_group_name_to_context    
class BannerPageView(TemplateView):
    template_name = "home/home.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # cargar todos los banners
        context["banners"] = Banner.objects.all()
        return context
        
@add_group_name_to_context    
class DashboardView(CustomTemplateView):
    template_name = "home/dashAdministracion.html"
    


