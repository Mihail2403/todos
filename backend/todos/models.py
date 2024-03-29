from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TODO(models.Model):
    text = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text
