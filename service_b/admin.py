from django.contrib import admin

# Register your models here.
# service_b/admin.py
from django.contrib import admin
from .models import UserProfileB

admin.site.register(UserProfileB)
