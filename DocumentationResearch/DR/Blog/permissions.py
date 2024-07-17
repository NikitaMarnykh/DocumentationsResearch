from rest_framework import permissions


class IsOwnerOrAdminOrAuthenticatedReadAndCreate(permissions.BasePermission):

    # Разрешение на просмотр и создание дано только пользователям прошедшим проверку подлинности
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # Разрешение на обновление дано только создателю, а удаление администратору и создателю
    def has_object_permission(self, request, view, obj):
        if view.action == "update" or view.action == "partial_update":
            return obj.owner == request.user

        return bool((request.user and request.user.is_staff) or (obj.owner == request.user))
