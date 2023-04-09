from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import *
from . import views

app_name = "tasks"

# URLs for Tasks
tasks_patterns = [
    path('projects/<int:project_id>/milestones/<int:milestone_id>/tasks/',
         include( [
            path('create/', TaskCreateView.as_view(), name='task_create'),
            path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
            path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
            path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
        ]
        )
    ),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create_alone'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', views.update_task, name="task_update"),
    path('tasks/<int:pk>/update-status/', views.update_task_status, name="task_update_status"),
]

    # URLs for Milestones
milestone_patterns = [
    path('<int:project_id>/milestones/', MilestoneListView.as_view(), name='milestone_list'),
    path('<int:project_id>/milestones/create', MilestoneCreateView.as_view(), name='milestone_create'),
    path('<int:project_id>/milestones/<int:pk>/', MilestoneDetailView.as_view(), name='milestone_detail'),
    path('<int:project_id>/milestones/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone_update'),
    path('<int:project_id>/milestones/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone_delete')
]

urlpatterns = [
    path('', ProjectListView.as_view(), name = 'index'),
    path('', include(milestone_patterns)),
    path('', include(tasks_patterns)),
]



# URLs for Projects
urlpatterns += [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]

# URLS for tests and development
urlpatterns += [
]
