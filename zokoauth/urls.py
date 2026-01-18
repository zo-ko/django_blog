from django.urls import path
from . import views
app_name='zokoauth'
urlpatterns = [
    path('register',views.user_rigister,name='register'),
    path('login',views.user_login,name='login'),
    path('send_email',views.send_email_captche)
]
