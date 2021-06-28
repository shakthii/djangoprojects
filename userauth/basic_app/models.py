from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    userobj = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_url = models.URLField(blank=True)
    portfolio_pics = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.userobj.username
