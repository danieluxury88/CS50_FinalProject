from django.urls import path
from . import views
from .views import *

app_name = "personal"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create-cycle/', views.create_cycle, name = 'create_cycle'),
    path('toggle_work_session/', views.toggle_work_session, name='toggle_work_session'),
    
]