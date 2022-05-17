from rest_framework import permissions


class IsContributorOrReadOnly(permissions.BasePermission):
    message = 'You have to be the author or contributor to be able to edit'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
