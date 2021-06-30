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
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('careers/', include('careers.urls', namespace='careers')),


    # django rest api
    path('api/applications', ApplicationList.as_view()),
    path('api/applications/<int:pk>', ApplicationRetrieveDestroy.as_view()),
    path('api/activities', ActivityList.as_view()),
    path('api/activities/<int:pk>', ActivityRetrieveDestroy.as_view()),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_url = None
admin.site.site_header = 'HuminImp Administration'
