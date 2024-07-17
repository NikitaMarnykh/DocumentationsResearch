from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment, Category
from .serializers import PostSerializer
from .permissions import IsOwnerOrAdminOrAuthenticatedReadAndCreate
from .filters import PostFilter
from . import serializers


# Представление API постов с возможностью фильтровать по названию и создателю,
# отдельный JSON каждого поста с возможностью удаления, обновления,
# создания для зарегистрированных пользователей'''
class PostViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = (IsOwnerOrAdminOrAuthenticatedReadAndCreate, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Представление API комментариев с возможностью фильтровать по названию и создателю,
# отдельный JSON каждого поста с возможностью удаления, обновления,
# создания для зарегистрированных пользователей'''
class CommentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsOwnerOrAdminOrAuthenticatedReadAndCreate, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Представление API категорий с возможностью фильтровать по названию и создателю,
# отдельный JSON каждого поста с возможностью удаления, обновления,
# создания для зарегистрированных пользователей'''
class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsOwnerOrAdminOrAuthenticatedReadAndCreate, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
