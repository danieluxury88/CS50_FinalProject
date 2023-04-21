from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "home"
urlpatterns = [
    # path('', views.HomeView.as_view(), name = 'index'),
    # path("login", views.login_view, name='login'),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),
    
    path('', views.index, name ='index'),
    path('missions', views.MissionView.as_view(), name ='missions'),
    path('today-report', views.TodayReportView.as_view(), name ='today-report'),
    path('yesterday-report', views.YesterdayReportView.as_view(), name ='yesterday-report'),
    path('cycle-report', views.CycleReportView.as_view(), name ='cycle-report'),
]
