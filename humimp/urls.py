"""humimp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from jobs.views import ApplicationList, ApplicationRetrieveDestroy
from activities.views import ActivityList, ActivityRetrieveDestroy
from blogs.views import BlogList, BlogRetrieveDestroy
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/applications', ApplicationList.as_view()),
    path('api/applications/<int:pk>', ApplicationRetrieveDestroy.as_view()),
    path('api/activities', ActivityList.as_view()),
    path('api/activities/<int:pk>', ActivityRetrieveDestroy.as_view()),
    path('api/blogs', BlogList.as_view()),
    path('api/blogs/<int:pk>', BlogRetrieveDestroy.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
