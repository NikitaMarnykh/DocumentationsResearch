from django.urls import include, path
from rest_framework import routers

from ToDo import views

router = routers.SimpleRouter()
router.register('', views.TaskListViewSet)

urlpatterns = (
            # Подключаем к роутеру списки задач
            path('api/', include(router.urls)),
)
