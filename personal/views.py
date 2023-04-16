from datetime import timedelta

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import formats, timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Challenge, Cycle, Date, DayRegister, Event, WorkSession

import json


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
    cycle = Cycle.objects.create( start_time=start_time, end_time=end_time )
    cycle.save()
    context = {"msg":"Cycle Created", "current_cycle": json.dumps(cycle.to_dict()) }
    return JsonResponse(context)


def start_work_session(request):
    # Logic to create the WorkSession object
    start_time = timezone.now()
    work_session = WorkSession.objects.create(start_time=start_time)

    # Convert the start_time to a Unix timestamp (in seconds)
    start_time_timestamp = int(start_time.timestamp())

    # You can customize the text field if you want, here I'm just using the id of the object
    text = f"WorkSession {work_session.id}"

    local_start_time = timezone.localtime(work_session.start_time, timezone=timezone.pytz.timezone('America/Guayaquil'))
    formatted_local_start_time = formats.date_format(local_start_time, "H:i")

    return JsonResponse({'id': work_session.id, 'text': text, 'start_time': start_time_timestamp, 'formatted_local_start_time': formatted_local_start_time})


def stop_work_session(request):
    current_time = timezone.now()
    work_session = WorkSession.get_current_work_session()
    if  work_session:
        work_session.end_time = current_time
        work_session.save()
    

    # You can customize the text field if you want, here I'm just using the id of the object
    text = f"WorkSession {work_session.id}"

    return JsonResponse({'id': work_session.id, 'text': text})


"""
UNUSED FUNCTION
"""
# def toggle_work_session(request):
#     if request.method == 'GET':
#         current_time = timezone.now()
#         work_session = WorkSession.get_current_work_session()
#         if not work_session:
#             work_session = WorkSession.objects.create(
#                 start_time=current_time,
#             )
#         else:
#             work_session.end_time = current_time
#         work_session.save()
#         return HttpResponse('WorkSession updated successfully.', status=200)
#     else:
#         return HttpResponse('Invalid request method.', status=400)