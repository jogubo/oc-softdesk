from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer
from contributors.models import Contributor


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        contributor = Contributor.objects.filter(user=self.request.user)

        return (
            Project.objects.filter(author=self.request.user)
            | Project.objects.filter(project_contributor__in=contributor)
        )
