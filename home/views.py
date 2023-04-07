from django.shortcuts import render
from django.views import View
from django.conf import settings


from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils import timezone

from .models import User
from personal.models import Cycle


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


class HomeView(View):
    def get(self, request):
        current_time = timezone.now()
        current_cycle = Cycle.objects.filter(
            start_time__lte=current_time,
            end_time__gte=current_time
        ).first()
        if not current_cycle:
            current_cycle = None
        else:
            cycle = current_cycle

        context= {"msg": "ok", "current_cycle":current_cycle}
        return render(request, 'home/index.html', context)
    
    
class TestView(View):
    def get(self, request):
        return render(request, 'home/test.html')