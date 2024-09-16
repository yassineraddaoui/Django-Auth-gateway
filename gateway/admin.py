from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('role', 'email')  # Customize as needed

