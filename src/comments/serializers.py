from rest_framework.serializers import ModelSerializer

from .models import Comment
from issues.models import Issue


class CommentSerializer(ModelSerializer):

    class Meta:

        model = Comment

        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time',
        ]
        read_only_fields = ('author', 'issue', 'created_time')

    def create(self, validated_data):
        author = self.context.get('request', None).user

        issue = Issue.objects.get(
            pk=self.context.get('view').kwargs['issue_id']
        )

        comment = Comment.objects.create(
            description=validated_data['description'],
            author=author,
            issue=issue,
        )

        comment.save()
        return comment
