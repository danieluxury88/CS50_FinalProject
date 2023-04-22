from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,HttpResponse, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import (View,CreateView, DeleteView, ListView,UpdateView)

from personal.models import Cycle
from .models import Milestone, Project, Task, Status
from .forms import TaskForm

import json


class CurrentCycleMixin(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context['current_cycle_str'] = current_cycle_str
        return context

    
# PROJECTS
#region project_region
class ProjectCreateView(CurrentCycleMixin, CreateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('home:missions')



class ProjectUpdateView(CurrentCycleMixin, UpdateView):
    model = Project
    template_name = 'tasks/project/project_form.html'
    fields = ['title', 'estimated_duration', 'status']
    success_url = reverse_lazy('home:missions')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        milestones = Milestone.objects.filter(project=project)
        context["milestones"] = milestones
        return context


class ProjectDeleteView(CurrentCycleMixin, DeleteView):
    model = Project
    template_name = 'tasks/project/project_confirm_delete.html'
    success_url = reverse_lazy('home:missions')

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('pk')
        return get_object_or_404(Project, id=project_id)
    
    
#endregion

# MILESTONES
#region milestone_region
class MilestoneCreateView(CurrentCycleMixin, CreateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project', 'due_date']
    success_url = reverse_lazy('home:missions')
        
    

class MilestoneUpdateView(CurrentCycleMixin, UpdateView):
    model = Milestone
    fields = ['title', 'estimated_duration', 'status', 'project', 'due_date']
    success_url = reverse_lazy('home:missions')

        
        
class MilestoneDeleteView(CurrentCycleMixin,DeleteView):
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

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'estimated_duration', 'priority', 'milestone', 'due_date']
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


class TaskUpdateView(CurrentCycleMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('home:missions')



def update_task(request, pk):
    model_instance = Task.objects.get(pk=pk)
    form = TaskForm(instance=model_instance)
    
    update_view = TaskUpdateView.as_view()
    return update_view(request, pk=pk, form=form)
        


class TaskDeleteView(CurrentCycleMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home:missions')


class TaskListView(CurrentCycleMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = 'status'

#endregion


@csrf_exempt
def update_task_status(request):
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