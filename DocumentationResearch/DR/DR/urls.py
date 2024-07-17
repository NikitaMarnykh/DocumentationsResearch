"""
URL configuration for DR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .yasg import urlpatterns as doc_urls

# Доступные эндпоинты

# http://127.0.0.1:8000/api/auth/users/
# http://127.0.0.1:8000/api/auth/users/me/
# http://127.0.0.1:8000/api/auth/users/confirm/
# http://127.0.0.1:8000/api/auth/users/resend_activation/
# http://127.0.0.1:8000/api/auth/users/set_password/
# http://127.0.0.1:8000/api/auth/users/reset_password/
# http://127.0.0.1:8000/api/auth/users/reset_password_confirm/
# http://127.0.0.1:8000/api/auth/users/set_username/
# http://127.0.0.1:8000/api/auth/users/reset_username/
# http://127.0.0.1:8000/api/auth/users/reset_username_confirm/
# http://127.0.0.1:8000/api/auth/
# http://127.0.0.1:8000/api/authorization/token/login/
# http://127.0.0.1:8000/api/authorization//token/logout/
# http://127.0.0.1:8000/api/api/JWT/token/
# http://127.0.0.1:8000/api/api/JWT/token/refresh/
# http://127.0.0.1:8000/api/verify/
# http://127.0.0.1:8000/api/baseauth/login/
# http://127.0.0.1:8000/api/baseauth/logout/
# http://127.0.0.1:8000/blog/api/posts/
# http://127.0.0.1:8000/blog/api/posts/<int:pk>
# http://127.0.0.1:8000/blog/api/categories/
# http://127.0.0.1:8000/blog/api/categories/<int:pk>
# http://127.0.0.1:8000/blog/api/comments/
# http://127.0.0.1:8000/blog/api/comments/<int:pk>
# http://127.0.0.1:8000/quotes/api/api/JWT/token/verify/
# http://127.0.0.1:8000/quotes/api/<int:pk>
# http://127.0.0.1:8000/todo/api/<int:pk>
# http://127.0.0.1:8000/todo/api/<int:pk>
# http://127.0.0.1:8000/spectacular/api/schema/
# http://127.0.0.1:8000/spectacular/api/schema/swagger-ui/
# http://127.0.0.1:8000/spectacular/api/schema/redoc/
# http://127.0.0.1:8000/yasg/swagger<format>/
# http://127.0.0.1:8000/yasg/swagger/
# http://127.0.0.1:8000/yasg/redoc/


urlpatterns = [
    # Админ панель
    path('admin/', admin.site.urls),
    # URL адреса Аунтефикации
    path('api/baseauth/', include('rest_framework.urls')),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/authorization/', include('djoser.urls.authtoken')),
    path('api/JWT/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/JWT/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/JWT/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # URL адреса приложения Blog
    path('blog/', include('Blog.urls')),
    # URL адреса приложения QuotesCentralBank
    path('quotes/', include('QuotesCentralBank.urls')),
    # URL адреса приложения ToDo
    path('todo/', include('ToDo.urls')),
    # drf-spectacular
    # YOUR PATTERNS
    path('spectacular/api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('spectacular/api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('spectacular/api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

# drf-yasg
urlpatterns += doc_urls
