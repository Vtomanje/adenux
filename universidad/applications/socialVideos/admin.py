from django.contrib import admin
from .models import SocialVideo

# Register your models here.

class SocialVideoAdmin(admin.ModelAdmin):
    exclude = ('uploaded_by',)

    def save_model(self, request, obj, form, change):
        if not obj.uploaded_by:
            obj.uploaded_by = request.user
        obj.save()

admin.site.register(SocialVideo, SocialVideoAdmin)
