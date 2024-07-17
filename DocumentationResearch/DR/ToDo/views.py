from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ToDo.models import TaskList
from ToDo.serializers import TaskListSerializer
from ToDo.permissions import IsOwnerOrAdminOrAuthenticatedReadAndCreate


# Представление API списка задач с возможностью фильтровать по названию и создателю,
# отдельный JSON каждого списка с возможностью удаления, обновления,
# создания для зарегистрированных пользователей'''
class TaskListViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsOwnerOrAdminOrAuthenticatedReadAndCreate, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Каждому пользователю показывает только его список задач, администратору все списки
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset().all()
        return super().get_queryset().filter(owner=self.request.user)
