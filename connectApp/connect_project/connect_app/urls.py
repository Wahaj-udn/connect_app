# connect_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('explore/', views.explore_page, name='explore'),
]
