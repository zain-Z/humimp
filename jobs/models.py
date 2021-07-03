from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator

REGION_TYPE = (
    ('Baghdad', "Baghdad"),
    ('Mousl', "Mousl"),
    ('Erbil', "Erbil"),
    ('Anbar', "Anbar"),
    ('Babylon', "Babylon"),
    ('Basra', "Basra"),
    ('Dhi Qar', "Dhi Qar"),
    ('Diyala', "Diyala"),
    ('Dohuk', "Dohuk"),
    ('Karbala', "Karbala"),
    ('KirKuk', "KirKuk"),
    ('Maysan', "Maysan"),
    ('Najaf', "Najaf"),
    ('Qaisiyah', "Qaisiyah"),
    ('Salahaddin', "Salahaddin"),
    ('Sulaymaniyah', "Sulaymaniyah"),
    ('Wasit', "Wasit"),
)

GENDER_TYPE = (
    ('Female', "Female"),
    ('Male', "Male"),
)


class Application(models.Model):

    full_name = models.CharField(max_length=200)

    email = models.EmailField(max_length=255, unique=True, db_index=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone number must be entered in the format: '+999999999'.\
             Up to 14 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17, unique=True)

    region = models.CharField(choices=REGION_TYPE, max_length=12)

    address = models.CharField(max_length=250, blank=True, null=True)

    gender = models.CharField(choices=GENDER_TYPE, max_length=6)

    english = models.CharField(
        default="English", max_length=7, blank=True, null=True)

    kurdish = models.CharField(
        default="Kurdish", max_length=7, blank=True, null=True)

    arabic = models.CharField(
        default="Arabic", max_length=6, blank=True, null=True)

    cover_letter = models.TextField()

    upload_cv = models.FileField(
        validators=[validate_file_extension],
        upload_to='uploadcv/')

    def __str__(self):
        return (self.phone)

    def __str__(self):
        return (self.full_name)

    def __str__(self):
        return (self.email)


class VisionMissionValue(models.Model):

    Vission_Mission_Value_desc1 = models.CharField(max_length=300, default='')

    Vission_Mission_Value_desc2 = models.CharField(max_length=300, default='')
    vission_text = models.CharField(max_length=300, default='')

    mission_text = models.CharField(max_length=300, default='')
    value_text = models.CharField(max_length=300, default='')


class WhatWeAreDoing(models.Model):
    image_bg_what_we_are_doing = models.FileField(
        validators=[validate_image_extension], upload_to='background/whatwe/', null=True, blank=True)
    image_header_logo_sticky_what_we_are_doing = models.FileField(
        validators=[validate_image_extension], upload_to='background/whatwe/', null=True, blank=True)
    image_footer_logo_what_we_are_doing = models.FileField(
        validators=[validate_image_extension], upload_to='background/whatwe/', null=True, blank=True)


class Donate(models.Model):
    image_bg_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/donate/', null=True, blank=True)
    image_header_logo_sticky_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/donate/', null=True, blank=True)
    image_footer_logo_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/donate/', null=True, blank=True)


class Volunteer(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', null=True, blank=True)
    image_header_logo_sticky_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', null=True, blank=True)
    image_footer_logo_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', null=True, blank=True)


class About(models.Model):
    image_bg_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_middle_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_header_logo_sticky_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_footer_logo_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)


class GetInvolved(models.Model):
    image_bg_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_careers_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_joinus_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_header_logo_sticky_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_footer_logo_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)


class WhoWeAre(models.Model):
    WhoWeAre_image1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    WhoWeAre_image2 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    WhoWeAre_image3 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    WhoWeAre_desc1 = models.CharField(max_length=300, default='')

    WhoWeAre_desc2 = models.CharField(max_length=300, default='')

    WhoWeAre_desc3 = models.CharField(max_length=300, default='')

    WhoWeAre_desc4 = models.CharField(max_length=300, default='')
    WhoWeAre_desc5 = models.CharField(max_length=300, default='')

    WhoWeAre_desc6 = models.CharField(max_length=300, default='')

    WhoWeAre_desc7 = models.CharField(max_length=300, default='')
    image_bg_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_left_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_middle_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_right_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_header_logo_sticky_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    image_footer_logo_who_we_are = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)


class Index(models.Model):
    slide_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    slide_title_index = models.CharField(max_length=300, default='')
    slide_subtitle_index = models.CharField(max_length=300, default='')

    image_bg_index_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_bg_index_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_bg_index_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    index_animals = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_index_stories_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_index_stories_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_index_stories_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_index_stories_four = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_footer_logo = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    image_header_logo_sticky = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)


class WhatWeAreDoingDetails(models.Model):
    WhatWeAreDoing_details_image_gallery = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    WhatWeAreDoing_details_image1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    WhatWeAreDoing_details_image2 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)
    WhatWeAreDoing_details_image3 = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    WhatWeAreDoing_details_name = models.CharField(max_length=300, default='')
    WhatWeAreDoing_details_desc1 = models.CharField(max_length=300, default='')

    WhatWeAreDoing_details_desc2 = models.CharField(max_length=300, default='')

    WhatWeAreDoing_details_desc3 = models.CharField(max_length=300, default='')

    WhatWeAreDoing_details_desc4 = models.CharField(max_length=300, default='')
    WhatWeAreDoing_details_desc5 = models.CharField(max_length=300, default='')

    WhatWeAreDoing_details_desc6 = models.CharField(max_length=300, default='')

    WhatWeAreDoing_details_desc7 = models.CharField(max_length=300, default='')
    image_bg_what_we_are_doing_details = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_right = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_middle = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_left = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_four = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_five = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_what_we_are_doing_details_sex = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_footer_logo_what_we_are_doing_details = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
    image_header_logo_sticky_what_we_are_doing_details = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeDetails/', null=True, blank=True)
