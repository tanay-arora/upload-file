from django.db import models
from django.utils.text import slugify
from event.models import ticket
from django.contrib.auth.hashers import make_password, check_password

class stay_informed(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self) -> str:
        return self.name

class subscriber(models.Model):
    email = models.EmailField()
    def __str__(self) -> str:
        return self.email

class attende(models.Model):
    name = models.CharField(max_length=126)
    contact = models.CharField(max_length=25)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    tshirt_size = models.CharField(max_length=8)
    linkedin = models.TextField()
    social_links = models.TextField(blank=True,null=True)
    country = models.CharField(max_length=240)
    college_name = models.CharField(max_length=360,blank=True,null=True)
    where_you_know = models.CharField(max_length=120,null=True)

class participants(models.Model):
    name = models.CharField(max_length=126)
    contact = models.CharField(max_length=25)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    tshirt_size = models.CharField(max_length=8)

class startup(models.Model):
    country = models.CharField(max_length=240)
    college_name = models.CharField(max_length=360,blank=True,null=True)
    linkedin = models.TextField()
    social_links = models.TextField(blank=True,null=True)
    website_url = models.TextField(blank=True,null=True)
    company_name = models.CharField(max_length=360)
    office_location = models.TextField(blank=True,null=True)
    total_employees = models.CharField(max_length=26,blank=True,null=True)
    pitchbook = models.FileField(upload_to="startup/pitchbook/",blank=True,null=True) 
    describe_one_sentence = models.TextField()
    core_problem = models.TextField()
    use_case = models.TextField(blank=True,null=True)
    target_audience = models.TextField(blank=True,null=True)
    business_model = models.TextField(blank=True,null=True)
    biggest_competitors = models.TextField(null=True)
    why_unique = models.TextField()
    raise_capital = models.TextField()
    video_url = models.TextField(blank=True,null=True)
    incubator_program = models.TextField(blank=True,null=True)
    company_category = models.CharField(max_length=120) 
    industry = models.CharField(max_length=120) 
    team_representative = models.ForeignKey(participants,on_delete=models.PROTECT)
    where_you_know = models.CharField(max_length=120,null=True) 
    showcasing_product = models.BooleanField(default=False)
    hiring_interns = models.BooleanField(default=False)
    hiring_professionals = models.BooleanField(default=False)
    cu_passout = models.BooleanField(default=False)
    have_revenue = models.BooleanField()
    is_proprietary = models.BooleanField(default=False)

class users(models.Model):
    username = models.EmailField(null=True)
    password = models.CharField(max_length=120,default="",editable=None)
    startup = models.ForeignKey(startup,on_delete=models.PROTECT,blank=True,null=True)
    attende = models.ForeignKey(attende,on_delete=models.PROTECT,blank=True,null=True)
    def __str__(self) -> str:
        return self.username

class transaction(models.Model):
    user = models.ForeignKey(users,on_delete=models.PROTECT)
    ticket = models.ForeignKey(ticket,on_delete=models.PROTECT)
    ticketid= models.CharField(max_length=17,null=True,default="",editable=None)
    def save(self, *args, **kwargs):
        self.ticketid="CUEFFECTUS#"+str('{:.5f}'.format(int(self.user.startup.id or self.user.attende.id)/100000)).replace('.','')
        super().save(*args, **kwargs)
