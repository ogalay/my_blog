from django.contrib import admin
from .models import Football_videos


class AdminVideos(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Football_videos, AdminVideos)
