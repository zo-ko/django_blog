from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()
class Blogcategory(models.Model):
    category_name=models.CharField(max_length=20,primary_key=True)

    class Meta:
        db_table='blogcategory'

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    pub_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Blogcategory,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='blog'

class Blogcomment(models.Model):
    content=models.TextField()
    pub_time=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='blogcomment'