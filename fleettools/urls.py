from django.urls import path

from . import views

app_name = 'fleettools'

urlpatterns = [
    path('', views.index, name='index'),
    path('fleetmover/', views.fleetmover, name='fleetmover'),
]
