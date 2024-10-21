from django.db import models


class EntryManager(models.Manager):
    """ porcedimiento para entradas"""
    
        
    def entradas_en_banner(self):
        #devuelve las ultimas 4 entradas en banner
        return self.filter(
            public=True,
            in_banner=True,
        ).order_by('-created')[:4]
        
