from django.db import models

# Create your models here.
class portfolioDetails(models.Model):
    #images
    image =models.ImageField(upload_to='static/assets/img')
    #summary
    summary =models.CharField(max_length=255)

    #link to project
    links = models.URLField(max_length=200)


   ## def __str__(self):
     #   return self.summary
  
    
