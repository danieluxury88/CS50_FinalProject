from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        context = {
            'installed': settings.INSTALLED_APPS,
        }
        return render(request, 'home/main.html', context)
