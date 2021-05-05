from django.contrib import admin
from .models import Activity, ActivityImage


class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 3


class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityImageInline, ]


admin.site.site_header = 'your_header'
admin.site.site_title = 'site_title'
admin.site.index_title = 'index_title'
admin.site.register(Activity, ActivityAdmin)
