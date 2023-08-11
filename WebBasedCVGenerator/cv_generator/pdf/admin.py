from django.contrib import admin
from .models import Profile

# changing admin header
admin.site.site_header = "CV Generator Admin Panel"
# changing admin title
admin.site.site_title = "CV Generator"
# changing admin index title
admin.site.index_title = "Manage models and groups"

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'email', 'phone', 'summary']
    filter_fields = ['name', 'email', 'phone', 'summary']
    ordering = ['name']
    list_per_page = 10


admin.site.register(Profile, ProfileAdmin)
