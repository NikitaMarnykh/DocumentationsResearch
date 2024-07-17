from django.contrib import admin

from ToDo.models import TaskList


# Добавляем модель Task List в админ панель
@admin.register(TaskList)
class AdminBlog(admin.ModelAdmin):
    pass
