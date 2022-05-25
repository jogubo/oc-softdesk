from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from .serializers import IssueSerializer
from projects.permissions import HasProjectPermission
from .permissions import IsAuthorOrReadOnly


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = (
        IsAuthenticated,
        HasProjectPermission,
        IsAuthorOrReadOnly
    )

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs['project_id'])

        queryset = project.issues.all()

        return queryset
