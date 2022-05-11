from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_id'])
