from django.contrib.auth import views as auth_views
from django.urls import path

from  .views import *

app_name = "tasks"
urlpatterns = [
    path('', test, name = 'test'),
]




urlpatterns += [
    # URLs for Projects
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    # URLs for Milestones
    path('milestones/', MilestoneListView.as_view(), name='milestone-list'),
    path('milestones/create/', MilestoneCreateView.as_view(), name='milestone-create'),
    path('milestones/<int:pk>/', MilestoneDetailView.as_view(), name='milestone-detail'),
    path('milestones/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone-update'),
    path('milestones/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone-delete'),

    # URLs for Tasks
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
