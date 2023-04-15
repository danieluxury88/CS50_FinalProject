from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils import timezone, formats

from .models import User
from personal.models import Cycle, WorkSession



def index(request):
    current_cycle = Cycle.get_current_cycle()
    work_session = WorkSession.get_current_work_session()

    context= {"msg": "ok", 
              "current_cycle":current_cycle,
              "work_session": work_session,
              }
    return render(request, "home/index.html", context)


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

    
    
class TestView(View):
    def get(self, request):
        current_cycle = Cycle.get_current_cycle()
        current_work_cycle = WorkSession.get_current_work_session()

        if current_work_cycle:
            start_time_timestamp  = int(current_work_cycle.start_time.timestamp())
            local_start_time = timezone.localtime(current_work_cycle.start_time, timezone=timezone.pytz.timezone('America/Guayaquil'))
            formatted_local_start_time = formats.date_format(local_start_time, "H:i")
            print(formatted_local_start_time)
            id= current_work_cycle.pk
            text = f"WorkSession {current_work_cycle.id}"
        else:
            formatted_local_start_time = None
            local_start_time = None
            start_time_timestamp = None
            id= None
            text = None

        context= {"msg": "ok",
                  "current_cycle":current_cycle,
                  "object":current_work_cycle, 'id': id, 'text': text, 'start_time': start_time_timestamp, "local_start_time": local_start_time,
                  'formatted_local_start_time': formatted_local_start_time}
        return render(request, 'home/test.html', context)
