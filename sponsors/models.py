from django.db import models
from django.utils.text import slugify

class investors(models.Model):
    name = models.CharField(max_length=126)
    image = models.ImageField(upload_to="past_speakers/")
    designation = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField()
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class sponsors(models.Model):
    title = models.CharField(max_length=140,null=True, blank=True)
    image = models.ImageField(upload_to="sponsors/")
    url = models.URLField(null=True,blank=True)
    data = models.JSONField(null=True,blank=True)
    slug = models.SlugField(editable=False,default='')
    def __str__(self) -> str:
        return self.title if self.title else str(self.id)

class sponsors_category(models.Model):
    title = models.CharField(max_length=140)
    data = models.JSONField(null=True,blank=True)
    sponsors = models.ManyToManyField(sponsors)
    def __str__(self) -> str:
        return self.title
