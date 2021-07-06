from django.contrib import admin
from .models import VisionMissionValue, Application, WhoWeAre, WhatWeAreDoing, Volunteer, Index, Donate, WhatWeAreDoingDetails, About, GetInvolved


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


class VisionMissionValueAdmin(admin.ModelAdmin):
    list_display = ['Vission_Mission_Value_desc1',
                    'Vission_Mission_Value_desc2',
                    'vission_text',
                    'mission_text',
                    'value_text',
                    ]


class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = ['WhoWeAre_image1',
                    'WhoWeAre_image2',
                    'WhoWeAre_image3',
                    'WhoWeAre_desc1',
                    'WhoWeAre_desc2',
                    'WhoWeAre_desc3',
                    'WhoWeAre_desc4',
                    'WhoWeAre_desc5',
                    'WhoWeAre_desc6',
                    'WhoWeAre_desc7',
                    'image_bg_who_we_are',
                    'image_left_who_we_are',
                    'image_middle_who_we_are',
                    'image_right_who_we_are',
                    'image_header_logo_sticky_who_we_are',
                    'image_footer_logo_who_we_are',
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
    list_display = ['slide_image_index',
                    'slide_title_index',
                    'slide_subtitle_index',
                    ]


class WhatWeAreDoingDetailsAdmin(admin.ModelAdmin):
    list_display = ['WhatWeAreDoing_details_image_gallery',
                    'WhatWeAreDoing_details_image1',
                    'WhatWeAreDoing_details_image2',
                    'WhatWeAreDoing_details_image3',
                    'WhatWeAreDoing_details_name',
                    'WhatWeAreDoing_details_desc1',
                    'WhatWeAreDoing_details_desc2',
                    'WhatWeAreDoing_details_desc3',
                    'WhatWeAreDoing_details_desc4',
                    'WhatWeAreDoing_details_desc5',
                    'WhatWeAreDoing_details_desc6',
                    'WhatWeAreDoing_details_desc7',
                    'image_bg_what_we_are_doing_details',
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
admin.site.register(WhoWeAre, WhoWeAreAdmin)
admin.site.register(WhatWeAreDoing, WhatWeAreDoingAdmin)
admin.site.register(WhatWeAreDoingDetails, WhatWeAreDoingDetailsAdmin)
