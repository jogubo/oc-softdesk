from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsContributorOrReadOnly
from contributors.models import Contributor


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrReadOnly]

    def get_queryset(self):
        contributor = Contributor.objects.filter(user=self.request.user)
        queryset = Project.objects.filter(
            Q(author=self.request.user)
            | Q(contributors__in=contributor)
        )
        return queryset.distinct()
