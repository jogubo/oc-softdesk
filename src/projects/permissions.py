from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from .models import Project


class IsProjectOwner(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            return request.user.is_author(project)

        else:
            return False


class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            return request.user.is_contributor(project)

        else:
            return False


class HasProjectPermission(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list', 'retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['project_id'])
            if request.user.is_author(project):
                return True
            if request.user.is_contributor(project):
                return True

        else:
            return False
