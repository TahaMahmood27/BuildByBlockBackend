from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    topic_Heading = models.CharField(max_length=200)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)