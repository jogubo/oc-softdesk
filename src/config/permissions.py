from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from projects.models import Project
from contributors.models import Contributor
from issues.models import Issue
from comments.models import Comment


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

        allowed_actions = ['create', 'list', 'retrieve']
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


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        allowed_basenames = ['issues', 'comments']
        if view.basename in allowed_basenames:
            if view.basename == 'issues':
                object = Issue
            if view.basename == 'comments':
                object = Comment
            allowed_basename = True

        allowed_actions = ['list', 'retrieve']
        if view.action in allowed_actions and allowed_basename:
            return True

        allowed_actions = ['update', 'destroy']
        if view.action in allowed_actions and allowed_basename:
            object = get_object_or_404(object, pk=view.kwargs['pk'])
            if request.user == object.author:
                return True

        else:
            return False
