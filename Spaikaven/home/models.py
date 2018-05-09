from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)

    def __str__(self):
        return self.message
