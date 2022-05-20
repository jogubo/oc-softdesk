from rest_framework.serializers import ModelSerializer

from .models import Comment


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
