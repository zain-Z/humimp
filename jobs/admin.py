from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'region',
                    'gender', 'language', 'cover_letter', 'upload_cv']


admin.site.register(Application, ApplicationAdmin)
