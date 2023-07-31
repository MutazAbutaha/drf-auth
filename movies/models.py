from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.title