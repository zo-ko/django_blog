from django import forms
from django.contrib.auth import get_user_model
from .models import captchamodel
user=get_user_model()

class registerform(forms.Form):
    username=forms.CharField(max_length=10,min_length=2,error_messages={
        'required':'请输入用户名',
        'max_length':'用户名不超过10位',
        'min_length':'用户名不少于2位'
    })
    email=forms.EmailField(error_messages={
        'required':'请输入邮箱',
        'invalid':'请输入正确的邮箱'
    })
    captcha=forms.CharField(max_length=10,min_length=4)
    password=forms.CharField(min_length=6,max_length=20)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        exist=user.objects.filter(email=email).exists()
        if exist:
            raise forms.ValidationError('邮箱已经存在')
        else:
            return email
    
    def clean_captcha(self):
        captcha=self.cleaned_data.get('captcha')
        email=self.cleaned_data.get('email')
        exist=captchamodel.objects.filter(email=email,captcha=captcha).first()
        if not exist:
            raise forms.ValidationError('验证码错误')
        exist.delete()
        return captcha