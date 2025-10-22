from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user
class CustomUser(AbstractUser):
    profile_pictures = models.ImageField(default="default.png")


# Profile 

class Profile(models.Model):
 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username
    


