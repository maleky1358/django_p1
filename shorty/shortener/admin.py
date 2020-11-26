from django.contrib import admin
from . import models

@admin.register(models.URLs)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'url_hash', 'clicks', 'created_at')
    fields = ['full_url', 'url_hash']
