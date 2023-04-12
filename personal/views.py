from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.utils import timezone
from datetime import timedelta

from .models import Cycle, Date, Challenge, Event, WorkSession, DayRegister

def index(request):
    cycle = Cycle.get_current_cycle()
    print(cycle)
    work_session = WorkSession.get_current_work_session()
        
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


def create_cycle(request):
    start_time = timezone.now()
    end_time = start_time + timedelta(hours=99, minutes =59, seconds =99)
    print(start_time, end_time)
    cycle = Cycle.objects.create( start_time=start_time, end_time=end_time )
    cycle.save()
    return JsonResponse({"msg":"Cycle Created"})





def toggle_work_session(request):
    if request.method == 'GET':
        current_time = timezone.now()
        work_session = WorkSession.get_current_work_session()
        if not work_session:
            work_session = WorkSession.objects.create(
                start_time=current_time,
            )
        else:
            work_session.end_time = current_time
        work_session.save()
        return HttpResponse('WorkSession updated successfully.', status=200)
    else:
        return HttpResponse('Invalid request method.', status=400)