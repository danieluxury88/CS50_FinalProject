from django.urls import path

from . import views
from .views import *

app_name = "personal"
urlpatterns = [
    path('create-cycle/', views.create_cycle, name = 'create_cycle'),
    path('start_work_session/', views.start_work_session, name='start_work_session'),
    path('stop_work_session/', views.stop_work_session, name='stop_work_session'),

    # urls.py
    path('work_sessions/', views.work_sessions_no_csrf, name='work_sessions'),
    path('register-event/', views.register_event, name='register_event'),    
]