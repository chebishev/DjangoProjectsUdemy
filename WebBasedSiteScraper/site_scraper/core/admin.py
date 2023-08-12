from django.contrib import admin
from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_per_page = 25


admin.site.register(Link, LinkAdmin)
