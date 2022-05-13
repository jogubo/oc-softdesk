from rest_framework.serializers import ModelSerializer

from .models import Issue
from projects.models import Project


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
            'author',
            'assignee_user',
            'created_time',
        ]

        read_only_fields = [
            'author',
            'project',
            'created_time',
        ]

    def create(self, validated_data):
        author = self.context.get('request', None).user

        assignee_user = self.context.get('request', None).user

        project = Project.objects.get(
            pk=self.context.get('view').kwargs['project_id']
        )

        issue = Issue.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            tag=validated_data['tag'],
            priority=validated_data['priority'],
            project=project,
            status=validated_data['status'],
            author=author,
            assignee_user=assignee_user,
        )
        issue.save()
        return issue

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
