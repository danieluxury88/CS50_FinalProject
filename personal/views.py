from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.http import JsonResponse
from django.utils import timezone

from .models import Cycle, Date, Challenge, Event 

def index(request):
    # return JsonResponse({"msg":"ok"})
    current_time = timezone.now()
    existing_cycle = Cycle.objects.filter(
        start_time__lte=current_time,
        end_time__gte=current_time
    ).first()
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
        

    dates = Date.objects.all()
    challenges = Challenge.objects.all()
    events = Event.objects.all()
    context = {"msg":"Current Cycle", 
               "current_cycle": cycle,
               "dates":dates,
               "challenges":challenges,
               "events":events}
    return render(request, "personal/personal_page.html", context)


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
