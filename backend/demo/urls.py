# todo/urls.py

from django.urls import path
from .views import home, TaskListView, TaskDetailView

urlpatterns = [
    path('', home),  # Homepage
    path('tasks/', TaskListView.as_view(), name='task-list'),           # GET & POST
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),  # PUT & DELETE
]
