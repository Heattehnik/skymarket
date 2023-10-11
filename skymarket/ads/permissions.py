from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Класс разрешения, который позволяет только владельцу редактировать объекты,
    а остальным пользователям разрешает только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение (GET, HEAD, OPTIONS) разрешено всем.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись (PUT, PATCH, DELETE) разрешено только владельцу.
        return obj.author == request.user
