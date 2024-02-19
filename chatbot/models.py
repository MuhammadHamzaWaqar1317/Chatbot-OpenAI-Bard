from django.db import models

# Create your models here.

class Chat(models.Model):
    message=models.TextField()
    response=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)