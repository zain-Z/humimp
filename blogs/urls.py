from django.urls import path
from . import views
from . import api

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('stories_and_blogs/', views.stories_and_blogs, name='stories_and_blogs'),
    path('teams/', views.teams, name='teams'),


    path('stories/', views.stories, name='story'),
    path('story_detail/<int:id>', views.stories_detail, name='stories_detail'),

    # api
    path('api/stories', api.stories_api, name='stories_api'),
    path('api/stories/<int:id>', api.story_detail_api, name='story_detail_api'),


    # class based views
    path('api/v2/stories', api.StoriesDetailListApi.as_view(),
         name='StoriesDetailListApi'),
    path('api/v2/stories/<int:id>',
         api.StoriesDetailDetail.as_view(), name='StoriesDetailDetail'),
]
