from django.urls import path
from . import views
urlpatterns = [
    path('register',views.user_rigister),
    path('login',views.user_login)
]
