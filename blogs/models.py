from django.db import models
from .validators import validate_image_extension


class Blog(models.Model):
    image_bg_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    image_blogs_right = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_middle = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_left = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    image_blogs_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_four = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_five = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_sex = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_seven = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_blogs_eight = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    image_footer_logo_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    image_header_logo_sticky_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)


class Story(models.Model):
    image_bg_story = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)

    image_story_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_four = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_five = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_sex = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_seven = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_story_eight = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)

    image_footer_logo_story = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)
    image_header_logo_sticky_story = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/', null=True, blank=True)


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


class Team(models.Model):
    image_bg_team = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)

    image_team_right = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)
    image_team_middle = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)
    image_team_left = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)

    image_footer_logo_team = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)
    image_header_logo_sticky_team = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)


class StoriesDetail(models.Model):
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
