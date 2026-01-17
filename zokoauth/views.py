from django.shortcuts import render
from django.http.response import JsonResponse
import random
from django.core.mail import send_mail
# Create your views here.

def user_rigister(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')

def send_email_captche(request):
    email=request.GET.get('email')
    if not email:
        return JsonResponse({'code':400,'message':'请输入邮箱'})
    ms="".join((random.sample(['1','2','3','4','5','6','7','8','9','0'],4)))
    send_mail('博客验证码',message=ms,recipient_list=[email],from_email=None)
    return JsonResponse({'code':200,'message':'验证码发送成功'})