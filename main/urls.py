"""Defines URL patterns for the main app."""
from django.urls import path
from . import views

appname = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact-details/', views.contact_details, name='contact_details'),
]