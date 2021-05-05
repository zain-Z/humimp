from rest_framework import serializers
from .models import Activity, ActivityImage


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ['id', 'title', 'date', 'location', 'description',
                  'image']


class ActivityImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityImage
        fields = ['id', 'image']
