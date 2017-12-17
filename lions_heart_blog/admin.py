from django.contrib import admin
from lions_heart_blog.models import Post, Comment, Image


class ImageInline(admin.TabularInline):
    model = Image


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class ItemAdmin(admin.ModelAdmin):
    inlines = (CommentInline, ImageInline)
