from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.http import JsonResponse
from django.utils import timezone

from .models import Cycle, Date, Challenge, Event, WorkSession, DayRegister

def index(request):
    current_time = timezone.now()
    cycle = get_current_cycle(current_time)
    work_session = get_current_work_session(current_time)
        
    dates = Date.objects.all()
    challenges = Challenge.objects.all()
    events = Event.objects.all()
    days = DayRegister.objects.all()

    context = {"msg":"Current Cycle",
               "work_session": work_session, 
               "current_cycle": cycle,
               "dates":dates,
               "challenges":challenges,
               "days":days,
               "events":events}
    return render(request, "personal/personal_page.html", context)


def get_current_work_session(current_time):
     work_session = WorkSession.objects.filter(start_time__lte=current_time, end_time__isnull=True).first()
     return work_session

def get_current_cycle(current_time):
    existing_cycle = Cycle.objects.filter( start_time__lte=current_time, end_time__gte=current_time).first()
    if not existing_cycle:
        end_time = current_time + timezone.timedelta(seconds= 99*3600 + 59*60 + 59)
        cycle = Cycle.objects.create(
            start_time=current_time,
            end_time=end_time
        )
        cycle.save()
        # return success response or redirect to cycle detail view
    else:
        cycle = existing_cycle
    return existing_cycle


def current_cycle(request):
    current_time = timezone.now()
    existing_cycle = Cycle.objects.filter(
        start_time__lte=current_time,
        end_time__gte=current_time
    ).first()
    if not existing_cycle:
        end_time = current_time + timezone.timedelta(seconds= 99*3600 + 59*60 + 59)
        current_cycle = Cycle.objects.create(
            start_time=current_time,
            end_time=end_time
        )
        current_cycle.save()
        # return success response or redirect to cycle detail view
    else:
        current_cycle = existing_cycle
        

    context = {"msg":"Current Cycle", "current_cycle": current_cycle}
    return render(request, "personal/personal_page.html", context)

class CycleDetailView(DetailView):
    model = Cycle

class CycleListView(ListView):
    model = Cycle
