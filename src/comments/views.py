from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .serializers import CommentSerializer
from issues.models import Issue
from .permissions import IsAuthorOrReadOnly
from projects.permissions import HasProjectPermission


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticated,
        HasProjectPermission,
        IsAuthorOrReadOnly
    )

    def get_queryset(self):
        queryset = Issue.objects.get(
            Q(project__id=self.kwargs['project_id'])
            & Q(pk=self.kwargs['issue_id'])
        )
        return queryset.comments.all()
