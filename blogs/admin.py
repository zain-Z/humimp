from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, BlogImage


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 3


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline, ]


admin.site.register(Blog, BlogAdmin)
