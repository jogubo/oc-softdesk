from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from projects.models import Project
from contributors.models import Contributor


class IsProjectOwner(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            if request.user == project.author:
                return True

        else:
            return False


class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            contributor = get_object_or_404(
                Contributor,
                user=request.user,
                project=project
            )
            if contributor in project.contributors.all():
                return True

        else:
            return False


class HasProjectPermission(BasePermission):
    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['project_id'])
            contributor = get_object_or_404(
                Contributor,
                user=request.user,
                project=project
            )
            if request.user == project.author:
                return True
            if contributor in project.contributors.all():
                return True

        else:
            return False


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        pass
