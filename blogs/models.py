from django.db import models
from .validators import validate_image_extension


from datetime import date


class Blog(models.Model):
    blogs_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    blogs_date = models.DateField(default=date.today)
    blogs_desc = models.CharField(max_length=300, default='')
    blogs_location = models.CharField(max_length=300, default='')


class Team(models.Model):
    teams_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)
    teams_name = models.CharField(max_length=300, default='')

    teams_desc = models.CharField(max_length=300, default='')


class StoryList(models.Model):
    stories_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)

    stories_date = models.DateField(default=date.today)
    stories_location = models.CharField(max_length=300, default='')
    stories_name = models.CharField(max_length=300, default='')


class StoriesDetail(models.Model):
    stories_details_image_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    stories_details_image_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    stories_details_image_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)

    stories_details_date = models.DateField(default=date.today)
    stories_details_location = models.CharField(max_length=300, default='')
    stories_details_name = models.CharField(max_length=300, default='')
    stories_details_desc1 = models.CharField(max_length=300, default='')
    stories_details_desc2 = models.CharField(max_length=300, default='')
    stories_details_desc3 = models.CharField(max_length=300, default='')
    stories_details_desc4 = models.CharField(max_length=300, default='')
    stories_details_desc5 = models.CharField(max_length=300, default='')
    stories_details_desc6 = models.CharField(max_length=300, default='')
    stories_details_desc7 = models.CharField(max_length=300, default='')

    # teaba
    image_stories_detail_one_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_two_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_three_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_four_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_five_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_sex_teaba = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)


class StoryAndBlog(models.Model):
    image_bg_stories_and_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)

    image_stories_and_blogs_left = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)
    image_stories_and_blogs_middle = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)

    image_footer_logo_stories_and_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)
    image_header_logo_sticky_stories_and_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)
