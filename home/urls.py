from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "home"
urlpatterns = [
    # path('', views.HomeView.as_view(), name = 'index'),

    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    path('test', views.TestView.as_view(), name ='test'),
    path('', views.index, name ='index'),

    path('create-cycle/', views.create_cycle, name = 'create_cycle'),

]
