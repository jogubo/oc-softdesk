from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import Comment
from .serializers import CommentSerializer

from issues.models import Issue


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # queryset = Comment.objects.filter(
        #     Q(p
        #     Q(issue=self.kwargs['issue_id'])
        # )

        queryset = Issue.objects.get(
            Q(project__id=self.kwargs['project_id'])
            & Q(pk=self.kwargs['issue_id'])
        )

        return queryset.comments.all()
