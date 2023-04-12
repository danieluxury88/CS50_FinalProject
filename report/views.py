from django.shortcuts import render
from django.http import JsonResponse

from personal.models import Cycle, Date, Event, DayRegister



def index(request):
    cycle = Cycle.get_current_cycle()
    dates = Date.get_dates_within_cycle(cycle)
    events = Event.get_events_within_cycle(cycle)
    days = DayRegister.get_registers_within_cycle(cycle)

    context = {"msg":"Current Cycle",
               "current_cycle": cycle,
               "dates": dates,
               "events": events,
               "days": days,
               }
    return render(request, "report/report.html", context)
