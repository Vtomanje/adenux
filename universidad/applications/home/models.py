from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# apps terceros
from model_utils.models import TimeStampedModel
from django.utils import timezone
from django.utils.timezone import now
from django.core.exceptions import PermissionDenied


class Banner(TimeStampedModel):
    """ Modelo de pagina de Banner """
    title = models.CharField('Titulo', max_length=256)
    title2 = models.CharField('Sub-Titulo', max_length=256)
    descripcion = models.TextField()
    contact_email = models.EmailField('email de contacto', blank=True, null=True)
    public = models.BooleanField(default=False)
    image = models.ImageField('Banner', upload_to='banner', blank=True, null=True)
    in_banner = models.BooleanField(default=False)
    phone = models.CharField('Telefono de contacto', max_length=20)
   
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        
    def __str__(self):
        
        return self.title
    





