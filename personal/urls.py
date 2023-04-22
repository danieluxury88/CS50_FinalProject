from django.urls import path

from . import views

app_name = "personal"
urlpatterns = [
    path('create-cycle/', views.create_cycle, name = 'create_cycle'),
    path('start_work_session/', views.start_work_session, name='start_work_session'),
    path('stop_work_session/', views.stop_work_session, name='stop_work_session'),
    path('register-event/', views.register_event, name='register_event'),    
]