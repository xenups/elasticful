
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet


from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION, SUGGESTER_PHRASE, SUGGESTER_TERM)

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,  SuggesterFilterBackend)

from App.document.task import *

from rest_framework import generics

from App import serializers
from App.models import Task
from App.serializers import TaskDocumentSerializer


class TaskDocumentView(DocumentViewSet):
    document = TaskDocument
    serializer_class = TaskDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,

    ]
    suggester_fields = {
        'title_suggest': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_TERM,
                SUGGESTER_PHRASE,
                SUGGESTER_COMPLETION,
            ],
        },
        'report_suggest': {
            'field': 'report.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },

    }

    search_fields = (
        'title',
        'report',
    )
    # Define filtering fields
    filter_fields = {
        'id': None,
        'title': 'title.raw',
        'report': 'report.raw',
    }
    # Define ordering fields
    ordering_fields = {
        'id': None,
        'title': None,
        'report': None,
    }


class TaskLists(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    report = None

    def get_object(self, queryset=None):
        return queryset.get(report=self.report)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
