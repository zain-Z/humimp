from django.contrib import admin
from .models import Blog, StoryList, StoryAndBlog, Team, StoriesDetail


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blogs_image',
                    'blogs_date',
                    'blogs_desc',
                    'blogs_location',
                    ]


class StoryListAdmin(admin.ModelAdmin):
    list_display = ['stories_image',
                    'stories_date',
                    'stories_location',
                    'stories_name',

                    ]


class StoryAndBlogAdmin(admin.ModelAdmin):
    list_display = ['image_bg_stories_and_blogs',
                    'image_stories_and_blogs_left',
                    'image_stories_and_blogs_middle',
                    'image_footer_logo_stories_and_blogs',
                    'image_header_logo_sticky_stories_and_blogs',
                    ]


class TeamAdmin(admin.ModelAdmin):
    list_display = ['teams_image',
                    'teams_name',
                    'teams_desc',
                    ]


class StoryListAdmin(admin.ModelAdmin):
    list_display = ['stories_image',
                    'stories_date',
                    'stories_location',
                    'stories_name',

                    ]


class StoriesDetailAdmin(admin.ModelAdmin):
    list_display = ['stories_details_image_one',
                    'stories_details_image_two',
                    'stories_details_image_three',
                    'stories_details_date',
                    'stories_details_location',
                    'stories_details_name',
                    'stories_details_desc1',
                    'stories_details_desc2',
                    'stories_details_desc3',
                    'stories_details_desc4',
                    'stories_details_desc5',
                    'stories_details_desc6',
                    'stories_details_desc7',

                    # teaba
                    'image_stories_detail_one_teaba',
                    'image_stories_detail_two_teaba',
                    'image_stories_detail_three_teaba',
                    'image_stories_detail_four_teaba',
                    'image_stories_detail_five_teaba',
                    'image_stories_detail_sex_teaba',
                    ]


admin.site.register(StoryAndBlog, StoryAndBlogAdmin)
admin.site.register(StoryList, StoryListAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(StoriesDetail, StoriesDetailAdmin)
admin.site.register(Blog, BlogAdmin)
