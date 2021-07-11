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


class Contact(models.Model):
    email_contact = models.CharField(max_length=300, default='')
    phone_contact = models.CharField(max_length=300, default='')


class Donate(models.Model):
    image_bg_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/donate/', null=True, blank=True)
    facebook_link = models.CharField(max_length=300, default='')
    twitter_link = models.CharField(max_length=300, default='')
    instagram_link = models.CharField(max_length=300, default='')
    location_donate = models.CharField(max_length=300, default='')
    email_donate = models.CharField(max_length=300, default='')
    phone_donate = models.CharField(max_length=300, default='')


class Volunteer(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', null=True, blank=True)


class About(models.Model):
    image_middle_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    text_about = models.CharField(max_length=300, default='')


class GetInvolved(models.Model):
    image_careers_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    text_careers_getinvolved = models.CharField(max_length=300, default='')
    image_joinus_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', null=True, blank=True)
    text_joinus_getinvolved = models.CharField(max_length=300, default='')


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


class Slider(models.Model):
    slide_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    slide_title_index = models.CharField(max_length=300, default='')
    slide_subtitle_index = models.CharField(max_length=300, default='')


class Index(models.Model):
    image_about_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    text_about_index = models.CharField(max_length=300, default='')
    text_what_we_are_doing_index = models.CharField(max_length=300, default='')
    image_story_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', null=True, blank=True)
    text_story_index = models.CharField(max_length=300, default='')


class WhatWeAreDoingDetail(models.Model):
    whatDoDetail_image_gallery = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoingDetails/', null=True, blank=True)

    whatDoDetail_image1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoingDetails/', null=True, blank=True)
    whatDoDetail_image2 = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoingDetails/', null=True, blank=True)
    whatDoDetail_image3 = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoingDetails/', null=True, blank=True)

    whatDoDetail_name = models.CharField(max_length=300, default='')
    whatDoDetail_desc1 = models.CharField(max_length=300, default='')

    whatDoDetail_desc2 = models.CharField(max_length=300, default='')

    whatDoDetail_desc3 = models.CharField(max_length=300, default='')

    whatDoDetail_desc4 = models.CharField(max_length=300, default='')
    whatDoDetail_desc5 = models.CharField(max_length=300, default='')

    whatDoDetail_desc6 = models.CharField(max_length=300, default='')

    whatDoDetail_desc7 = models.CharField(max_length=300, default='')
