from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer
from App.models import Task

# Name of the Elasticsearch index
task_INDEX = Index('task')
# See Elasticsearch Indices API reference for available settings
task_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@task_INDEX.doc_type
class TaskDocument(DocType):
    class Meta:
        model = Task
        fields = [
            'title',
            'id',
            'report',
        ]
