from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

   


    def __str__(self):
        return f'Title: {self.title}\n Content: {self.content}\n Date:{self.date_posted}\n Author: {self.user}\n Completed: {self.completed}'
    
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk':self.pk})