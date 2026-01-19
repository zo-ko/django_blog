from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
import random
from django.core.mail import send_mail
from .models import captchamodel
from .forms import registerform,loginform
from django.contrib.auth import get_user_model,login,logout
# Create your views here.

user=get_user_model()

def user_rigister(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        form=registerform(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user.objects.create_user(email=email,username=username,password=password)
            return redirect(reverse('zokoauth:login'))
        else:
            print(form.errors)
            return redirect(reverse('zokoauth:register'))
        

def user_logout(request):
    logout(request)
    return redirect(reverse('blog:index'))
        
@require_http_methods(['GET','POST'])
def user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        form=loginform(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            remember=form.cleaned_data.get('remember')
            use=user.objects.filter(email=email).first()
            if use and use.check_password(password):
            #     return HttpResponse(use.username)
            # else:
            #     return HttpResponse(use.username)
                login(request,use)
                if not remember:
                    request.session.set_expiry(0)
                
                return redirect(reverse('blog:index'))
            else:
                print('邮箱或者密码错误')
                return redirect(reverse('zokoauth:login'))
def send_email_captche(request):
    email=request.GET.get('email')
    if not email:
        return JsonResponse({'code':400,'message':'请输入邮箱'})
    ms="".join((random.sample(['1','2','3','4','5','6','7','8','9','0'],4)))
    captchamodel.objects.update_or_create(email=email,defaults={'captcha':ms})
    send_mail('博客验证码',message=ms,recipient_list=[email],from_email=None)
    return JsonResponse({'code':200,'message':'验证码发送成功'})