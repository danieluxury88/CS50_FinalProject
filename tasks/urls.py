from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import *
from . import views

app_name = "tasks"

# URLs for Tasks
tasks_patterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create_alone'),
    path('tasks/<int:pk>/update/', views.update_task, name="task_update"),
    path('tasks/<int:pk>/update-status/', views.update_task_status, name="task_update_status"),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update-task-due-date/', views.update_task_due_date, name="task_update_due_date"),
    
]

    # URLs for Milestones
milestone_patterns = [
    path('<int:project_id>/milestones/create', MilestoneCreateView.as_view(), name='milestone_create'),
    path('<int:project_id>/milestones/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone_update'),
    path('<int:project_id>/milestones/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone_delete'),
    path('milestones/create', MilestoneCreateView.as_view(), name='milestone_single_create'),
    path('milestones/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone_single_update'),
    path('milestones/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone_single_delete'),
    path('milestones/<int:pk>/update-milestone-due-date/', views.update_milestone_due_date, name="milestone_update_due_date"),
]

urlpatterns = [
    path('', include(milestone_patterns)),
    path('', include(tasks_patterns)),
]



# URLs for Projects
urlpatterns += [
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]

# URLS for tests and development
urlpatterns += [
]
