from django.conf.urls import url
from rest_framework import routers

from App import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'task', views.TaskDocumentView, base_name='task')
urlpatterns = [
    path('tasks/', views.TaskLists.as_view(report="hello mashti")),
    path('tasks/<int:pk>/', views.TaskDetails.as_view()),
    url(r'^tasker/', include(router.urls)),

]
