from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import formats, timezone
from django.views import View

from personal.models import Cycle, WorkSession

from .models import User
from personal.models import Cycle, WorkSession
from tasks.models import Project,Milestone, Task, DueDateChoice

from datetime import timedelta
import json


def index(request):
    current_cycle = Cycle.get_current_cycle()

    if current_cycle:
        current_cycle_str = json.dumps(current_cycle.to_dict())
    else:
        current_cycle_str = None

    current_work_session = WorkSession.get_current_work_session()

    if current_work_session:
        work_session_start_time_timestamp  = int(current_work_session.start_time.timestamp())
        local_start_time = timezone.localtime(current_work_session.start_time, timezone=timezone.pytz.timezone('America/Guayaquil'))
        formatted_local_start_time = formats.date_format(local_start_time, "H:i")
    else:
        work_session_start_time_timestamp = None

    tasks_without_milestones = Task.objects.filter(milestone__isnull=True, due_date=DueDateChoice.DUE_TODAY.value).order_by('priority')

    today_work_sessions = WorkSession.get_today_work_sessions()
    today_total_work_session_duration = WorkSession.get_todays_work_sessions_duration()


    context= {"msg": "ok", 
              "current_cycle_str":current_cycle_str,
              "work_session_start_time": work_session_start_time_timestamp,
              "tasks_without_milestones": tasks_without_milestones,
              "today_work_sessions":today_work_sessions,
              "today_total_work_session_duration":today_total_work_session_duration,
              }
    return render(request, "home/index.html", context)


class MissionView(View):
    def get(self, request):
        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None


        projects = Project.objects.all()
        # independent_tasks = Task.objects.filter(milestone__isnull=True).exclude(due_date=DueDateChoice.COMPLETED.value).exclude(status='COMPLETED').order_by('priority').order_by('due_date')
        independent_tasks = Task.objects.filter(milestone__isnull=True).order_by('-status').order_by('due_date').order_by('priority').order_by('due_date')

        context= {
                  "current_cycle_str":current_cycle_str,
                  "projects":projects,
                   "independent_tasks": independent_tasks,
              }
        return render(request, 'home/missions.html', context)
    

class TestView(View):
    def get(self, request):
        current_cycle = Cycle.get_current_cycle()
        if current_cycle:
            current_cycle_str = json.dumps(current_cycle.to_dict())
        else:
            current_cycle_str = None

        context= {
                  "current_cycle_str":current_cycle_str,
              }
        return render(request, 'home/test.html', context)



#region authentication

def login_view(request):
    if request.method == "POST":
        print("login attempt")
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home:index"))
        else:
            return render(request, "home/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "home/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "home/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home:index"))
    else:
        return render(request, "home/register.html")
    
#endregion

    
    
