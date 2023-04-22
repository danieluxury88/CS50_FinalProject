from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,HttpResponse, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.decorators.csrf import csrf_exempt

from .models import Milestone, Project, Task, Status
from personal.models import Cycle
from .forms import TaskForm

import json


# PROJECTS
#region project_region
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('home:missions')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context



class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('home:missions')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        milestones = Milestone.objects.filter(project=project)
        context['milestones'] = milestones

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'tasks/project/project_confirm_delete.html'
    success_url = reverse_lazy('home:missions')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context
    
#endregion

# MILESTONES
#region milestone_region
class MilestoneListView(ListView):
    model = Milestone


class MilestoneDetailView(DetailView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project', 'due_date']

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
    fields = ['title', 'estimated_duration', 'status', 'project', 'due_date']
    
    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            # return reverse('tasks:project_detail', args=[project_id])
            return reverse('home:missions')
        except:
            return reverse('home:missions')
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context
    

class MilestoneUpdateView(UpdateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project', 'due_date']

    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            # return reverse('tasks:project_detail', args=[project_id])
            return reverse('home:missions')
        except:
            return reverse('home:missions')
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context
        
        
class MilestoneDeleteView(DeleteView):
    model = Milestone
    success_url = reverse_lazy('tasks:project_detail')

    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            return reverse('tasks:project_detail', args=[project_id])
        except:
            return reverse('home:index')
    
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

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context



class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'estimated_duration', 'priority', 'milestone', 'due_date']
    success_url = reverse_lazy('tasks:milestone_detail')

    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            milestone_id = self.kwargs['milestone_id']
            return reverse('tasks:milestone_detail', args=[project_id, milestone_id])
        except:
            return reverse('home:missions')
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('home:index')

    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            milestone_id = self.kwargs['milestone_id']
            return reverse('tasks:milestone_detail', args=[project_id, milestone_id])
        except:
            return reverse('home:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        # Add your additional context here
        return context

def update_task(request, pk):
    model_instance = Task.objects.get(pk=pk)
    form = TaskForm(instance=model_instance)
    
    update_view = TaskUpdateView.as_view()
    return update_view(request, pk=pk, form=form)
        


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:milestone_detail')
    def get_success_url(self):
        try:
            project_id = self.kwargs['project_id']
            milestone_id = self.kwargs['milestone_id']
            return reverse('tasks:milestone_detail', args=[project_id, milestone_id])
        except:
            return reverse('home:index')
#endregion


@csrf_exempt
def update_task_status(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("status") is not None:
            id = data["id"]
            task = Task.objects.get(pk=id)
            status = data["status"]
            task.status = status
            task.save()

            status_str = Status(status)
            status_str_rep = status_str.name.replace('_', ' ')
            return JsonResponse({"msg": "OK", "status": status_str_rep})
        if data.get("msg") is not None:
            print(data["msg"])
        return JsonResponse({"msg": "OMG OK"})

    # Task must be updated via  PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)


@csrf_exempt
def update_task_due_date(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("due_date") is not None:
            id = data["id"]
            task = Task.objects.get(pk=id)
            due_date = data["due_date"]
            task.due_date = due_date
            task.save()
            return JsonResponse({"msg": "OK"})
        if data.get("msg") is not None:
            print(data["msg"])
        return JsonResponse({"msg": "OMG OK"})

    # Task must be updated via  PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)
    

@csrf_exempt
def update_milestone_due_date(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("due_date") is not None:
            id = data["id"]
            milestone = Milestone.objects.get(pk=id)
            due_date = data["due_date"]
            milestone.due_date = due_date
            milestone.save()
            return JsonResponse({"msg": "OK"})
        if data.get("msg") is not None:
            print(data["msg"])
        return JsonResponse({"msg": "OMG OK"})

    # Task must be updated via  PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)