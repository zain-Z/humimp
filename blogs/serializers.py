from rest_framework import serializers
from .models import Blog, BlogImage


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'date', 'location', 'description',
                  'image']


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = ['id', 'image']
