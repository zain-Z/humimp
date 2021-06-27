from rest_framework import serializers
from .models import CareerDetail


class CareerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetail
        fields = ['image_bg_career',
                  'title',
                  'description',
                  'contract_duration',
                  'job_type',
                  'job_shift',
                  'location',
                  'posted',
                  'minimum_education',
                  'minimum_experience',
                  'required_travel',
                  'no_of_jobs',
                  'deadline',
                  'image_footer_logo_career_detail',
                  'image_header_logo_sticky_career_detail',
                  ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise serializers.ValidationError(
                {"job_type": "Service is required"})
        return job_type
