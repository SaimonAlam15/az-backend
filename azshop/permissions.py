from rest_framework import permissions


class IsReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to access the method.
    """
    def has_permission(self, request, view):
        return request.method == 'GET' or (request.user and request.user.is_superuser)
    

class IsRestricted(permissions.BasePermission):
    """
    Custom permission to only allow superusers to access the method.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_superuser)