from django.contrib import admin
from .models import Blog, Post, Author, Moderator


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Moderator, ModeratorAdmin)
