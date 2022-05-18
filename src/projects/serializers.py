from rest_framework.serializers import ModelSerializer

from .models import Project
from contributors.serializers import ContributorSerializer


class ProjectSerializer(ModelSerializer):
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author',
            'contributors',
        ]
        read_only_fields = ('author',)

    def create(self, validated_data):
        author = self.context.get('request', None).user

        project = Project.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            type=validated_data['type'],
            author=author,
        )
        project.save()

        return project
