from django.urls import path
from . import views

app_name = "social_app"

urlpatterns = [
    path('video/', views.SocialVideoView.as_view(), name='video'),  # Vista para mostrar el video existente
   
]
