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
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    teams_name = models.CharField(max_length=300, default='')

    teams_desc = models.CharField(max_length=300, default='')


class Story(models.Model):
    stories_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    stories_date = models.DateField(default=date.today)
    stories_location = models.CharField(max_length=300, default='')
    stories_name = models.CharField(max_length=300, default='')


class StoriesDetail(models.Model):
    stories_details_image1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    stories_details_image2 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    stories_details_image3 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

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

    image_bg_stories_detail = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)

    image_stories_detail_right = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_middle = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_left = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)

    image_stories_detail_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_four = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_five = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_stories_detail_sex = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)

    image_footer_logo_stories_detail = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    image_header_logo_sticky_stories_detail = models.FileField(
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
