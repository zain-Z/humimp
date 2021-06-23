from rest_framework import serializers
from .models import Application, WhatWeAreDoing, Volunteer, Index, Donate, WhatWeAreDoingDetails
from django.core.mail import send_mail


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'phone', 'region', 'address',
                  'gender', 'english', 'arabic', 'kurdish', 'cover_letter', 'upload_cv']


class WhatWeAreDoingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatWeAreDoing
        fields = ['image_bg_what_we_are_doing',
                  'image_header_logo_sticky_what_we_are_doing',
                  'image_footer_logo_what_we_are_doing',
                  ]


class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        fields = ['image_bg_donate',
                  'image_header_logo_sticky_donate',
                  'image_footer_logo_donate',
                  ]


class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = ['image_bg_volunteer',
                  'image_header_logo_sticky_volunteer',
                  'image_footer_logo_volunteer',
                  ]


class WhatWeAreDoingDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatWeAreDoingDetails
        fields = ['image_bg_what_we_are_doing_details',
                  'image_what_we_are_doing_details_right',
                  'image_what_we_are_doing_details_middle',
                  'image_what_we_are_doing_details_left',
                  'image_what_we_are_doing_details_one',
                  'image_what_we_are_doing_details_two',
                  'image_what_we_are_doing_details_three',
                  'image_what_we_are_doing_details_four',
                  'image_what_we_are_doing_details_five',
                  'image_what_we_are_doing_details_sex',
                  'image_footer_logo_what_we_are_doing_details',
                  'image_header_logo_sticky_what_we_are_doing_details',
                  ]


class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = ['image_bg_index_one',
                  'image_bg_index_two',
                  'image_bg_index_three',
                  'index_animals',
                  'image_index_stories_one',
                  'image_index_stories_two',
                  'image_index_stories_three',
                  'image_index_stories_four',
                  'image_footer_logo',
                  'image_header_logo_sticky',
                  ]
