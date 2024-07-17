from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

# Подключаем к роутеру посты
router.register('posts', views.PostViewSet)

# Подключаем к роутеру комментарии
router.register('comments', views.CommentViewSet)

# Подключаем к роутеру категории
router.register('categories', views.CategoryViewSet)

urlpatterns = (
    path('api/', include(router.urls)),
)
