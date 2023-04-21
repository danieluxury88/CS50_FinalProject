from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import formats, timezone
from django.http import HttpResponseBadRequest

from .models import Cycle, Event, EventType, WorkSession

import json
from django.views.decorators.csrf import csrf_exempt
import datetime



# views.py
from django.core import serializers


def work_sessions(request):
    if request.method == "GET":
        work_sessions = WorkSession.objects.all()
        return render(request, 'personal/work_sessions.html', {'work_sessions': work_sessions})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            start_time = timezone.now()
            end_time_str = data.get('end_time')
            end_time = timezone.make_aware(datetime.datetime.fromisoformat(end_time_str)) if end_time_str else None
            work_session = WorkSession.objects.create(start_time=start_time, end_time=end_time)
            work_session.save()
            serialized_work_session = serializers.serialize('json', [work_session])
            return JsonResponse({'work_session': serialized_work_session})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")


@csrf_exempt
def work_sessions_no_csrf(request):
    return work_sessions(request)

        

def register_event(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            event_type = EventType.objects.get(pk= data.get('event_type'))
            date = timezone.now()
            event = Event.objects.create(date=date, event_type=event_type, title = event_type.title)
            event.save()
            serialized_event = serializers.serialize('json', [event])
            return JsonResponse({'event': serialized_event})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
    else:
        return JsonResponse({'event': "none"})


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
