from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'summary']
    filter_fields = ['name', 'email', 'phone', 'summary']
    ordering = ['name']


admin.site.register(Profile, ProfileAdmin)
