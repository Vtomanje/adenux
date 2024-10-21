from django import forms
from .models import SocialVideo, User

class SocialVideoForm(forms.ModelForm):
    class Meta:
        model = SocialVideo
        fields = ["user","title", "video_file"]

