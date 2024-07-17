from django.contrib import admin

from QuotesCentralBank.models import Quote


# Добавляем модель Quote в админ панель
@admin.register(Quote)
class AdminBlog(admin.ModelAdmin):
    pass
