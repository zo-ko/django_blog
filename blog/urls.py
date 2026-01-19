from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<blog_id>',views.blog_detail),
    path('pub',views.blog_pub),
]
