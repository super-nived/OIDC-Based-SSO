# service_b/urls.py
from django.urls import path
from .views import home, login, callback, protected_resource

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
    path('protected_resource/', protected_resource, name='protected_resource'),
]
