from django.db import models
from .validators import validate_file_extension
from django.core.validators import RegexValidator

JOB_TYPE = (
    ('1', "Baghdad"),
    ('2', "Mousl"),
    ('3', "Erbil"),
    ('4', "Anbar"),
    ('5', "Babylon"),
    ('6', "Basra"),
    ('7', "Dhi Qar"),
    ('8', "Diyala"),
    ('9', "Dohuk"),
    ('10', "Karbala"),
    ('11', "KirKuk"),
    ('12', "Maysan"),
    ('13', "Najaf"),
    ('14', "Qaisiyah"),
    ('15', "Salahaddin"),
    ('16', "Sulaymaniyah"),
    ('17', "Wasit"),
)

GENDER_TYPE = (
    ('1', "Female"),
    ('2', "Male"),
)

LANGUAGE_TYPE = (
    ('1', "English"),
    ('2', "Arabic"),
    ('3', "Kurdish"),
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
    region = models.CharField(choices=JOB_TYPE, max_length=2)
    gender = models.CharField(choices=GENDER_TYPE, max_length=1)
    language = models.CharField(choices=LANGUAGE_TYPE, max_length=1)
    cover_letter = models.TextField()
    upload_cv = models.FileField(
        validators=[validate_file_extension],
        upload_to='uploaded_files/')

    def __str__(self):
        return (self.phone)

    def __str__(self):
        return (self.full_name)

    def __str__(self):
        return (self.email)
