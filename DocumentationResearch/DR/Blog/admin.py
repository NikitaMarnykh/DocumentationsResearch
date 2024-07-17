from django.contrib import admin
from Blog.models import Post, Comment, Category


# Добавляем модели Post, Comment, Category в админ панель
@admin.register(Post, Comment, Category)
class AdminBlog(admin.ModelAdmin):
    pass
