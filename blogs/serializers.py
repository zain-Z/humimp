from rest_framework import serializers
from .models import Blog, Story, StoryAndBlog, Team, StoriesDetail


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['image_bg_blogs',
                  'image_blogs_right',
                  'image_blogs_middle',
                  'image_blogs_left',
                  'image_blogs_one',
                  'image_blogs_two',
                  'image_blogs_three',
                  'image_blogs_four',
                  'image_blogs_five',
                  'image_blogs_sex',
                  'image_blogs_seven',
                  'image_blogs_eight',
                  'image_footer_logo_blogs',
                  'image_header_logo_sticky_blogs',
                  ]


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['image_bg_story',
                  'image_story_one',
                  'image_story_two',
                  'image_story_three',
                  'image_story_four',
                  'image_story_five',
                  'image_story_sex',
                  'image_story_seven',
                  'image_story_eight',
                  'image_footer_logo_story',
                  'image_header_logo_sticky_story',
                  ]


class StoryAndBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryAndBlog
        fields = ['image_bg_stories_and_blogs',
                  'image_stories_and_blogs_left',
                  'image_stories_and_blogs_middle',
                  'image_footer_logo_stories_and_blogs',
                  'image_header_logo_sticky_stories_and_blogs',
                  ]


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['image_bg_team',
                  'image_team_right',
                  'image_team_middle',
                  'image_team_left',
                  'image_footer_logo_team',
                  'image_header_logo_sticky_team',
                  ]


class StoriesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoriesDetail
        fields = ['image_bg_stories_detail',
                  'image_stories_detail_right',
                  'image_stories_detail_middle',
                  'image_stories_detail_left',
                  'image_stories_detail_one',
                  'image_stories_detail_two',
                  'image_stories_detail_three',
                  'image_stories_detail_four',
                  'image_stories_detail_five',
                  'image_stories_detail_sex',
                  'image_footer_logo_stories_detail',
                  'image_header_logo_sticky_stories_detail',
                  ]
