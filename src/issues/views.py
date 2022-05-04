from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()
