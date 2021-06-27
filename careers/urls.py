from django.urls import path
from . import views


urlpatterns = [
    path('careerdetail', views.careerdetail, name='careerdetail'),
]
