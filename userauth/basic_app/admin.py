from django.contrib import admin

# Register your models here.
from basic_app.models import UserProfile

admin.site.register(UserProfile)
