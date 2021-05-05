from rest_framework import serializers
from .models import Application
from django.core.mail import send_mail


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'phone', 'region',
                  'gender', 'language', 'cover_letter', 'upload_cv']
