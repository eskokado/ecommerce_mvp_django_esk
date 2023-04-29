from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_authenticated and request.user.is_superuser
