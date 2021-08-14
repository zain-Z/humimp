from rest_framework import serializers
from .models import Blog, StoryDetail, StoryAndBlog, Team


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class StoryAndBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryAndBlog
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class StoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryDetail
        fields = '__all__'
        ordering = ['-story_date']
