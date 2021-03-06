from jobs.serializers import SliderSerializer
from django.contrib import admin
from .models import Contact, Slider, VisionMissionValue, Application, WhoWeAre, Volunteer, Index, Donate, WhatWeAreDoingDetail, About, GetInvolved


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'region', 'address',
                    'gender', 'english', 'arabic', 'kurdish', 'cover_letter', 'upload_cv']


class DonateAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_donate',
                    'facebook_link',
                    'twitter_link',
                    'instagram_link',
                    'location_donate',
                    'email_donate',
                    'phone_donate',

                    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'full_name',
                    'email',
                    'phone',
                    'subject',
                    'message',
                    ]


class GetInvolvedAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_careers_getinvolved',
                    'image_joinus_getinvolved',
                    'text_careers_getinvolved',
                    'text_joinus_getinvolved',
                    ]


class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'WhoWeAre_image1',
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

                    ]


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_volunteer',

                    ]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about',
                    'image_middle_about',

                    ]


class VisionMissionValueAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'Vission_Mission_Value_desc1',
                    'Vission_Mission_Value_desc2',
                    'vission_text',
                    'mission_text',
                    'value_text',

                    ]


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
                    'slide_subtitle_index',

                    ]


class IndexAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about_index',
                    'text_about_index_ar',
                    'image_about_index',
                    'image_story_index',
                    'text_story_index',
                    'whatDoDetail_text',
                    'whatDoDetail_text_ar',



                    ]


class WhatWeAreDoingDetailAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'whatDoDetail_image_gallery',
                    'whatDoDetail_image1',
                    'whatDoDetail_image2',
                    'whatDoDetail_image3',
                    'whatDoDetail_name',
                    'whatDoDetail_desc1',
                    'whatDoDetail_desc2',
                    'whatDoDetail_desc3',
                    'whatDoDetail_desc4',
                    'whatDoDetail_desc5',
                    'whatDoDetail_desc6',
                    'whatDoDetail_desc7',
                    'whatDoDetail_icon_name',
                    ]


admin.site.register(Index, IndexAdmin)
admin.site.register(Slider, SliderAdmin)

admin.site.register(GetInvolved, GetInvolvedAdmin)
admin.site.register(Donate, DonateAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhoWeAre, WhoWeAreAdmin)
admin.site.register(VisionMissionValue, VisionMissionValueAdmin)
admin.site.register(WhatWeAreDoingDetail, WhatWeAreDoingDetailAdmin)
