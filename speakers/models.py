from django.db import models
from django.utils.text import slugify

class current_speakers(models.Model):
    name = models.CharField(max_length=126)
    image = models.ImageField(upload_to="past_speakers/")
    designation = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField()
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class past_speakers(models.Model):
    name = models.CharField(max_length=126)
    image = models.ImageField(upload_to="past_speakers/")
    designation = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField()
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name
