from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = "account_app"

urlpatterns = [
    
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
  
    
]
