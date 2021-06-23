from django.contrib import admin
from .models import Application, WhatWeAreDoing, Volunteer, Index, Donate, WhatWeAreDoingDetails, About, GetInvolved


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'region', 'address',
                    'gender', 'english', 'arabic', 'kurdish', 'cover_letter', 'upload_cv']


class WhatWeAreDoingAdmin(admin.ModelAdmin):
    list_display = ['image_bg_what_we_are_doing',
                    'image_header_logo_sticky_what_we_are_doing',
                    'image_footer_logo_what_we_are_doing',
                    ]


class DonateAdmin(admin.ModelAdmin):
    list_display = ['image_bg_donate',
                    'image_header_logo_sticky_donate',
                    'image_footer_logo_donate',
                    ]


class GetInvolvedAdmin(admin.ModelAdmin):
    list_display = ['image_bg_getinvolved',
                    'image_careers_getinvolved',
                    'image_joinus_getinvolved',
                    'image_header_logo_sticky_getinvolved',
                    'image_footer_logo_getinvolved',
                    ]


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['image_bg_volunteer',
                    'image_header_logo_sticky_volunteer',
                    'image_footer_logo_volunteer',
                    ]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['image_bg_about',
                    'image_middle_about',
                    'image_header_logo_sticky_about',
                    'image_footer_logo_about',
                    ]


class IndexAdmin(admin.ModelAdmin):
    list_display = ['image_bg_index_one',
                    'image_bg_index_two',
                    'image_bg_index_three',
                    'index_animals',
                    'image_index_stories_one',
                    'image_index_stories_two',
                    'image_index_stories_three',
                    'image_index_stories_four',
                    'image_footer_logo',
                    'image_header_logo_sticky',
                    ]


class WhatWeAreDoingDetailsAdmin(admin.ModelAdmin):
    list_display = ['image_bg_what_we_are_doing_details',
                    'image_what_we_are_doing_details_right',
                    'image_what_we_are_doing_details_middle',
                    'image_what_we_are_doing_details_left',
                    'image_what_we_are_doing_details_one',
                    'image_what_we_are_doing_details_two',
                    'image_what_we_are_doing_details_three',
                    'image_what_we_are_doing_details_four',
                    'image_what_we_are_doing_details_five',
                    'image_what_we_are_doing_details_sex',
                    'image_footer_logo_what_we_are_doing_details',
                    'image_header_logo_sticky_what_we_are_doing_details',
                    ]


admin.site.register(Index, IndexAdmin)
admin.site.register(GetInvolved, GetInvolvedAdmin)
admin.site.register(Donate, DonateAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhatWeAreDoing, WhatWeAreDoingAdmin)
admin.site.register(WhatWeAreDoingDetails, WhatWeAreDoingDetailsAdmin)
