from django.contrib import admin

# Register your models here.
# service_a/admin.py
from django.contrib import admin
from .models import UserProfileA

admin.site.register(UserProfileA)
