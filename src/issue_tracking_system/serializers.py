from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author']
        read_only_fields = ('author',)


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'project',
            'status',
            'assignee_user',
            'created_time',
        ]


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
        read_only_fields = ('author',)
