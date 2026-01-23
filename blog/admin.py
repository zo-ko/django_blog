from django.contrib import admin
from .models import Blog,Blogcategory,Blogcomment
# Register your models here.

class Blogcategoryadmin(admin.ModelAdmin):
    list_display=['category_name']

class Blogadmin(admin.ModelAdmin):
    list_display=['title','content','pub_time','category','author']

class Blogcommentadmin(admin.ModelAdmin):
    list_display=['content','pub_time','blog','author']


admin.site.register(Blogcategory,Blogcategoryadmin)
admin.site.register(Blog,Blogadmin)
admin.site.register(Blogcomment,Blogcommentadmin)