from django.contrib import admin
from .models import Post, post_comment
# Registerq your models here.


class admin_post(admin.ModelAdmin):
    list_display = ["title", ]


class admin_comment(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')


admin.site.register(Post, admin_post)
admin.site.register(post_comment, admin_comment)
