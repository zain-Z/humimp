from django.urls import path
from . import views
from django.contrib import admin
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('applicantsList/', views.applicantsList, name='applicantsList'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('what_we_are_doing/', views.what_we_are_doing, name='what_we_are_doing'),
    path('donate/', views.donate, name='donate'),
    path('about/', views.about, name='about'),
    path('who_we_are/', views.who_we_are, name='who_we_are'),
    path('get_involved/', views.get_involved, name='get_involved'),
    path('what_we_are_doing_details/', views.what_we_are_doing_details,
         name='what_we_are_doing_details'),
]
