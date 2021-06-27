from django.urls import path
from . import views
from django.contrib import admin
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('story/', views.story, name='story'),
    path('stories_and_blogs/', views.stories_and_blogs, name='stories_and_blogs'),
    path('teams/', views.teams, name='teams'),
    path('stories_detail/', views.stories_detail, name='stories_detail'),
]