from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from projects.models import Project


class IsProjectOwner(BasePermission):

    def has_permission(self, request, view):
        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            if request.user == project.author:
                return True
            else:
                return False
