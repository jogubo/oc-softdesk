from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from projects.models import Project
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.get(
            Q(pk=self.kwargs['project_id']),
            Q(author=self.request.user)
            | Q(project_contributor__user=self.request.user)
        )
        return queryset.issue_related.all()
