from django.db import models
from django.utils.text import slugify

class summits(models.Model):
    title = models.CharField(max_length=120)
    data = models.JSONField(null=True,blank=True)
    slug = models.SlugField(editable=False,default='')
    def __str__(self) -> str:
        return self.title
    def save(self):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save()

class events(models.Model):
    title = models.CharField(max_length=240)
    subtitle = models.CharField(max_length=240,null=True,blank=True)
    From = models.TimeField(null=True)
    To = models.TimeField(null=True)
    summit = models.ForeignKey(summits,on_delete=models.PROTECT)
    location = models.TextField(null=True)
    data = models.JSONField(null=True,blank=True)
    slug = models.SlugField(editable=False,default='')
    def __str__(self) -> str:
        return self.title
    def save(self):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save()

class event_day(models.Model):
    title = models.CharField(max_length=120,null=True,blank=True)
    date = models.DateField()
    events = models.ManyToManyField(events)
    def __str__(self) -> str:
        return self.title if self.title else str(self.id)

class feature(models.Model):
    title = models.CharField(max_length=240)
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.title

class ticket(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField()
    features = models.ManyToManyField(feature)
    not_available = models.ManyToManyField(feature,related_name="not_available",blank=True)
    cost = models.CharField(max_length=12)
    data = models.JSONField(null=True,blank=True)
    slug = models.SlugField(editable=False,default='',null=True)
    def __str__(self) -> str:
        return self.title
    def save(self):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save()


