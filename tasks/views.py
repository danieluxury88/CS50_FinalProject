from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
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
    success_url = reverse_lazy('tasks:project_list')

# UpdateView for Projects
class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('tasks:project_list')

# DeleteView for Projects
class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('tasks:project_list')


# ListView for Milestones
class MilestoneListView(ListView):
    model = Milestone

# DetailView for Milestones
class MilestoneDetailView(DetailView):
    model = Milestone
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        milestone = self.get_object()
        context['num_tasks'] = milestone.tasks.count()
        context['num_completed_tasks'] = milestone.tasks.filter(status='COMPLETED').count()
        context['total_estimated_duration'] = milestone.tasks.aggregate(Sum('estimated_duration'))['estimated_duration__sum']
        context['total_left_estimated_duration'] = milestone.tasks.exclude(status='COMPLETED').aggregate(Sum('estimated_duration'))['estimated_duration__sum']

        return context

# CreateView for Milestones
class MilestoneCreateView(CreateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']
    success_url = reverse_lazy('tasks:milestone_list')

# UpdateView for Milestones
class MilestoneUpdateView(UpdateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']
    success_url = reverse_lazy('tasks:milestone_list')

# DeleteView for Milestones
class MilestoneDeleteView(DeleteView):
    model = Milestone
    success_url = reverse_lazy('tasks:milestone_list')


# ListView for Tasks
class TaskListView(ListView):
    model = Task
    ordering = 'status'
    # queryset = Task.objects.filter(status='COMPLETED')
    # queryset = Task.objects.exclude(status='COMPLETED')

    # status = self.request.GET.get('status', 'COMPLETED') TODO: when making dynamic search
    # return WorkItem.objects.filter(status=status)

# DetailView for Tasks
class TaskDetailView(DetailView):
    model = Task

# CreateView for Tasks
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('tasks:task_list')

# UpdateView for Tasks
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('tasks:task_list')

# DeleteView for Tasks
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
