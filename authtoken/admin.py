from django.contrib import admin

# Register your models here.
from .models import User,Organization
admin.site.register(User)
admin.site.register(Organization)
