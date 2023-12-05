# service_b/models.py
from django.db import models

class UserProfileB(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # Add other fields we needed
