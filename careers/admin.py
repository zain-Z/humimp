from django.contrib import admin
from .models import CareerDetail


class CareerDetailAdmin(admin.ModelAdmin):
    list_display = ['image_bg_career',
                    'title',
                    'description',
                    'contract_duration',
                    'job_type',
                    'job_shift',
                    'location',
                    'posted',
                    'minimum_education',
                    'minimum_experience',
                    'required_travel',
                    'no_of_jobs',
                    'deadline',
                    'image_footer_logo_career_detail',
                    'image_header_logo_sticky_career_detail',
                    ]


admin.site.register(CareerDetail, CareerDetailAdmin)
