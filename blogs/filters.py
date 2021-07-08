import django_filters
from .models import StoriesDetail


class StoriesDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StoriesDetail
        fields = '__all__'
        exclude = ['stories_details_image_one',
                   'stories_details_image_two',
                   'stories_details_image_three',
                   # teaba
                   'image_stories_detail_one_teaba',
                   'image_stories_detail_two_teaba',
                   'image_stories_detail_three_teaba',
                   'image_stories_detail_four_teaba',
                   'image_stories_detail_five_teaba',
                   'image_stories_detail_sex_teaba',

                   'id']
