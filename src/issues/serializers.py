from rest_framework.serializers import ModelSerializer

from .models import Issue


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
