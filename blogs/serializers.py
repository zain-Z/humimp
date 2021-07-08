from rest_framework import serializers
from .models import Blog, StoryList, StoryAndBlog, Team, StoriesDetail


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class StoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryList
        fields = '__all__'


class StoryAndBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryAndBlog
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class StoriesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoriesDetail
        fields = '__all__'
