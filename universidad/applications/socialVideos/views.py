import time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.models import User, Group
from .models import SocialVideo
from .mixins import LoginYSuperUsuarioMixin
from .forms import SocialVideoForm



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

##### Vista del video para like, dislkes y comentarios ###################################################
@add_group_name_to_context 
class SocialVideoView(LoginYSuperUsuarioMixin, View):
    form_class = SocialVideoForm
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        posts = SocialVideo.objects.all()

        context = {"form": form, "posts": posts}

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("home/home.html")

        context = {"form": form}

        return render(request, self.template_name, context)


# Vista para agregar likes
class AddLikeView(View):
    def post(self, request, video_id):
        video = get_object_or_404(SocialVideo, id=video_id)

        # Manejo de dislikes
        if request.user in video.dislike.all():
            video.dislike.remove(request.user)  # Quita dislike si ya existe

        # Manejo de likes
        if request.user in video.like.all():
            video.like.remove(request.user)  # Si ya le dio like, lo quitamos
        else:
            video.like.add(request.user)  # Si no ha dado like, lo agregamos

        return redirect('home_app:video_list')  # Redirigir a la lista de videos o a otro lugar

# Vista para agregar dislikes
class AddDislikeView(View):
    def post(self, request, video_id):
        video = get_object_or_404(SocialVideo, id=video_id)

        # Manejo de likes
        if request.user in video.like.all():
            video.like.remove(request.user)  # Quita like si ya existe

        # Manejo de dislikes
        if request.user in video.dislike.all():
            video.dislike.remove(request.user)  # Si ya le dio dislike, lo quitamos
        else:
            video.dislike.add(request.user)  # Si no ha dado dislike, lo agregamos

        return redirect('home_app:video_list')  # Redirigir a la lista de videos o a otro lugar
