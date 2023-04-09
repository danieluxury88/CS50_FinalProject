from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,HttpResponse, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.decorators.csrf import csrf_exempt

from .models import Milestone, Project, Task
from .forms import TaskForm

import json


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
        context['f_creation_time'] = timezone.localtime(milestone.creation_time).strftime('%B %d')
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
    fields = ['title', 'status', 'estimated_duration', 'priority', 'project']

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        return reverse('tasks:project_detail', args=[project_id])
    

class MilestoneDeleteView(DeleteView):
    model = Milestone
    success_url = reverse_lazy('tasks:project_detail')

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        return reverse('tasks:project_detail', args=[project_id])
    
 # endregion


# TASKS
# region task_region
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = 'status'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['test'] = "joseu"
        return context


class TaskDetailView(DetailView):
    model = Task



class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'estimated_duration', 'priority', 'milestone']
    success_url = reverse_lazy('tasks:milestone_detail')

    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            milestone_id = self.kwargs['milestone_id']
            return reverse('tasks:milestone_detail', args=[project_id, milestone_id])
        except:
            return reverse('tasks:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'status', 'estimated_duration', 'priority', 'milestone']
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


def update_task(request, pk):
    model_instance = Task.objects.get(pk=pk)
    form = TaskForm(instance=model_instance)
    update_view = UpdateView.as_view(
        model=Task,
        form_class=TaskForm,
        template_name='tasks/task_form.html'
    )
    return update_view(request, pk=pk, form=form)


@csrf_exempt
def update_task_status(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("status") is not None:
            id = data["id"]
            task = Task.objects.get(pk=id)
            task.status = data["status"]
            print(data["status"])
            task.save()
        return JsonResponse({"msg": "OK"})
        data = json.loads(request.body)
        if data.get("msg") is not None:
            print(data["msg"])
        return JsonResponse({"msg": "OMG OK"})

    # Task must be updated via  PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)
    return JsonResponse({"msg": "Link Ok"})