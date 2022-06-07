from rest_framework import permissions
# from django.contrib.auth.models import User

class FollowerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST" or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj or request.user.is_authenticated