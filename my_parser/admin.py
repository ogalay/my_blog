from django.contrib import admin
from .models import News
# Registerq your models here.


class admin_news(admin.ModelAdmin):
    list_display = ["title", "subtitle", "url"]


admin.site.register(News, admin_news)


