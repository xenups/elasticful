from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from App.models import Task
from  App.document.task import TaskDocument


class TaskDocumentSerializer(DocumentSerializer):
    class Meta:
        document = TaskDocument
        fields = ('title', 'report',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'report',)

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        task.title = validated_data['title']
        task.report_data = validated_data['report']
        task.save()
        return task
