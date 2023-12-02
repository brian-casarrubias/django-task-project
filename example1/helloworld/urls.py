from django.urls import path
from . views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name='home-page'),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(), name='task-update'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
   
    
]

 