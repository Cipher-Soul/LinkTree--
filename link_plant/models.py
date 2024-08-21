from django.db import models

# Create your models here.

# profile table
class Profile(models.Model):
    BG_CHOICES = (
        ('blue',"Blue"),
        ('yellow',"Yellow"),
        ('green',"Green"),
        ('crimson',"Crimson"),
    )
     # name,slug,bg_color
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length = 40,choices=BG_CHOICES)
    
    def __str__(self):
       return f"_{self.name}"
   
   
#    Link table
class Link(models.Model):
    text = models.CharField(max_length=200)
    url = models.URLField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="links")
    
    def __str__(self):
        return f"{self.url} || {self.text} || {self.profile}"
