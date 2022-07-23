from django.db import models
from django.utils.text import slugify

class gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return str(self.id)
