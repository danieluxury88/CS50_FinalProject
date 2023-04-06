from django.urls import path
from . import views
from .views import *

app_name = "personal"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('', CycleDetailView.as_view(), name = 'index'),
    path('<int:pk>', CycleListView.as_view(), name = 'index'),
    path('current_cycle/', current_cycle, name='current_cycle'),
    # path('<int:pk>', CycleUpdateView.as_view(), name = 'index'),
]