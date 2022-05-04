from rest_framework.viewsets import ModelViewSet

from .models import Project

class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)
