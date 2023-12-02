from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=150)


    def __str__(self):
        return f'{self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)