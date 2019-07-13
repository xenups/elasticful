from django.shortcuts import render
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend, FunctionalSuggesterFilterBackend)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# Create your views here.

from django_elasticsearch_dsl_drf.constants import (
    # ...
    FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
    FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
    SUGGESTER_COMPLETION)

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
        FunctionalSuggesterFilterBackend,
    ]
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
