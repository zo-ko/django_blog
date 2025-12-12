from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('detail/<blog_id>',views.blog_detail),
    path('pub',views.blog_pub),
]
