from django.contrib import admin
from .models import CareerDetail, CareerList, CareerDetatilImage


class CareerListAdmin(admin.ModelAdmin):
    list_display = ['image_bg_career_list',
                    'image_header_logo_sticky_career_list',
                    'image_footer_logo_career_list',
                    ]


class CareerDetatilImageAdmin(admin.ModelAdmin):
    list_display = ['image_header_logo_sticky_career_detail_image',
                    'image_footer_logo_career_detail_image',
                    ]


admin.site.register(CareerDetail)
admin.site.register(CareerList, CareerListAdmin)
admin.site.register(CareerDetatilImage, CareerDetatilImageAdmin)
