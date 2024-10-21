from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_group')
    search_fields = ('user__username',)  # Solo probamos con el nombre de usuario
    list_filter = ('user',)  # Solo el usuario por ahora

    def user_group(self, obj):
        # Obtener grupos del usuario, evitar error si no tiene grupos
        return " - ".join([group.name for group in obj.user.groups.all()]) or "Sin grupo"

    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)



