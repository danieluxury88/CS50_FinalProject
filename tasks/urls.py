from django.contrib.auth import views as auth_views
from django.urls import path

from  .views import *

app_name = "tasks"
urlpatterns = [
    path('', ProjectListView.as_view(), name = 'index'),
]




urlpatterns += [
    # URLs for Projects
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    # URLs for Milestones
    path('milestones/', MilestoneListView.as_view(), name='milestone_list'),
    path('milestones/create/', MilestoneCreateView.as_view(), name='milestone_create'),
    path('milestones/<int:pk>/', MilestoneDetailView.as_view(), name='milestone_detail'),
    path('milestones/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone_update'),
    path('milestones/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone_delete'),

    # URLs for Tasks
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
