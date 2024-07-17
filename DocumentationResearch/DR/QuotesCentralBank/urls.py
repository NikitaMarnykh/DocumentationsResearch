from django.urls import path, include
from rest_framework import routers

from .views import QuotesViewSet

router = routers.SimpleRouter()

# подключаем к роутеру котировки
router.register('', QuotesViewSet)

urlpatterns = (

    path('api/', include(router.urls)),
)

