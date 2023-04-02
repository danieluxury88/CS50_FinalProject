from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Milestone, Project, Task


def test(request):
    return JsonResponse({"msg":"ok"})


# ListView for Projects
class ProjectListView(ListView):
    model = Project

# DetailView for Projects
class ProjectDetailView(DetailView):
    model = Project

# CreateView for Projects
class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('project-list')

# UpdateView for Projects
class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('project-list')

# DeleteView for Projects
class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')


# ListView for Milestones
class MilestoneListView(ListView):
    model = Milestone

# DetailView for Milestones
class MilestoneDetailView(DetailView):
    model = Milestone

# CreateView for Milestones
class MilestoneCreateView(CreateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']
    success_url = reverse_lazy('milestone-list')

# UpdateView for Milestones
class MilestoneUpdateView(UpdateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']
    success_url = reverse_lazy('milestone-list')

# DeleteView for Milestones
class MilestoneDeleteView(DeleteView):
    model = Milestone
    success_url = reverse_lazy('milestone-list')


# ListView for Tasks
class TaskListView(ListView):
    model = Task

# DetailView for Tasks
class TaskDetailView(DetailView):
    model = Task

# CreateView for Tasks
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('task-list')

# UpdateView for Tasks
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('task-list')

# DeleteView for Tasks
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
