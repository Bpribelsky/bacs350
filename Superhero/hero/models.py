from django.db import models
class SuperHero(models.Model):
    
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=80)
    
    
    def __str__(self):
        return self.identity
    
    def get_absolute_url(self): 
        return ('/home/')