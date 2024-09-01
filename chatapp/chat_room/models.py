from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)