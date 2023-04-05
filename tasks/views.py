from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Milestone, Project, Task


def test(request):
    return JsonResponse({"msg":"ok"})

# PROJECTS
#region project_region
class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/project/project_list.html'


class ProjectDetailView(ListView):
    model = Project
    template_name = 'tasks/project/project_detail.html'
    context_object_name = 'milestones'

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        return Milestone.objects.filter(project=project)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        context['project'] = project
        return context


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('tasks:project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('tasks:project_list')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'tasks/project/project_confirm_delete.html'
    success_url = reverse_lazy('tasks:project_list')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)
    
#endregion

# MILESTONES
#region milestone_region
class MilestoneListView(ListView):
    model = Milestone


class MilestoneDetailView(DetailView):
    model = Milestone

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        milestone = self.get_object()
        context['tasks'] = milestone.tasks.all()
        context['num_tasks'] = milestone.tasks.count()
        context['num_completed_tasks'] = milestone.tasks.filter(status='COMPLETED').count()
        context['total_estimated_duration'] = milestone.tasks.aggregate(Sum('estimated_duration'))['estimated_duration__sum']
        context['total_left_estimated_duration'] = milestone.tasks.exclude(status='COMPLETED').aggregate(Sum('estimated_duration'))['estimated_duration__sum']
        return context
    

class MilestoneCreateView(CreateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']
    
    def get_success_url(self):
        project_id = self.kwargs['project_id']
        return reverse('tasks:project_detail', args=[project_id])
    

class MilestoneUpdateView(UpdateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project']

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        return reverse('tasks:project_detail', args=[project_id])
    

class MilestoneDeleteView(DeleteView):
    model = Milestone
    success_url = reverse_lazy('tasks:project_detail')

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        print(project_id)
        return reverse('tasks:project_detail', args=[project_id])
    
 # endregion


# TASKS
# region task_region
class TaskListView(ListView):
    model = Task
    ordering = 'status'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('tasks:milestone_detail')

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        milestone_id = self.kwargs['milestone_id']
        return reverse('tasks:milestone_detail', args=[project_id, milestone_id])


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'estimated_duration', 'status', 'milestone']
    success_url = reverse_lazy('tasks:milestone_detail')

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        milestone_id = self.kwargs['milestone_id']
        return reverse('tasks:milestone_detail', args=[project_id, milestone_id])


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:milestone_detail')

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        milestone_id = self.kwargs['milestone_id']
        return reverse('tasks:milestone_detail', args=[project_id, milestone_id])

#endregion