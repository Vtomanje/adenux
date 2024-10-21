from django.contrib.auth import authenticate, login
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from .models import Profile

from django import forms



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
class ProfileView(TemplateView):
    template_name = "profile/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if user.is_superuser:
            # Si el usuario autenticado es un superusuario, obtener todos los usuarios del grupo 'estudiantes'
            students_group = Group.objects.get(name='estudiantes')
            users = students_group.user_set.all()
            context['users'] = users  # Agrega esta línea para asignar los usuarios al contexto
        

        return context


