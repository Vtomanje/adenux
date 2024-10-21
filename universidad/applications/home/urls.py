from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.BannerPageView.as_view(), name='home'),  # Página de inicio
    path('dash-Admin/', views.DashboardView.as_view(), name='dashAdministracion'),  # Dashboard de administración
   
]
