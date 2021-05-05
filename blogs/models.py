from django.db import models
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):

    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="uploaded_files/")

    def __str__(self):
        return (self.title)


class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploaded_files/")
