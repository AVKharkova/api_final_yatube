from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Кастомное разрешение на корректировку и удаление контента автором.'''

    def has_permission(self, request, view):
        # Аннонимам разрешаем GET-запросы
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
