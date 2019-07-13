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


# there is 2 ways to define your serializer in document
# a way is that you define a
@task_INDEX.doc_type
class TaskDocument(DocType):
    # id = fields.IntegerField(attr='id')
    # title = fields.StringField(
    #     fields={
    #         'raw': fields.StringField(analyzer='keyword'),
    #         'suggest': fields.CompletionField(),
    #     }
    # )
    # report = fields.StringField(
    #     fields={
    #         'raw': fields.StringField(analyzer='keyword'),
    #         'suggest': fields.CompletionField(),
    #     }
    # )

    class Meta:
        model = Task
        fields = [
            'title',
            'id',
            'report',
        ]
