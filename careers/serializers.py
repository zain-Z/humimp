from rest_framework import serializers
from .models import CareerDetail


class CareerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetail
        fields = '__all__'
