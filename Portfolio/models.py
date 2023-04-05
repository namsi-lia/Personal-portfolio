from django.db import models
from any_urlfield.models import AnyUrlField


# Create your models here.
class portfolioDetails(models.Model):
    #images
    image =models.ImageField(upload_to='static/assets/img')
    #summary
    summary =models.CharField(max_length=255)

    #link to project
    #links = models.URLField(max_length=200)
    url = AnyUrlField("URL", null=True)
  

   ## def __str__(self):
     #   return self.summary
  
    
