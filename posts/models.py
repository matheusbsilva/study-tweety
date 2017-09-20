from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=150)
    likes = models.IntegerField(blank=True,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return self.text

    class Meta:
        ordering = ('created','likes')
