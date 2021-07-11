from rest_framework import serializers
from .models import Application,Slider, WhatWeAreDoing, Contact,VisionMissionValue, WhoWeAre, Volunteer, Index, Donate, WhatWeAreDoingDetails, About, GetInvolved
from django.core.mail import send_mail


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'phone', 'region', 'address',
                  'gender', 'english', 'arabic', 'kurdish', 'cover_letter', 'upload_cv']
                  
class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class WhatWeAreDoingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatWeAreDoing
        fields = '__all__'


class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = '__all__'


class GetInvolvedSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetInvolved
        fields = '__all__'


class WhoWeAreSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhoWeAre
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class WhatWeAreDoingDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatWeAreDoingDetails
        fields = '__all__'


class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class VisionMissionValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisionMissionValue
        fields = '__all__'
