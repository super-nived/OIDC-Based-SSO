from django.db import models


class UserProfileA(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # Add other fields we needed

