from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Blogcategory,Blog
from .forms import pubblogform
from django.http.response import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def blog_detail(request,blog_id):
    return render(request,'blog_detail.html')

@require_http_methods(['GET','POST'])
@login_required(login_url=reverse_lazy('zokoauth:login'))
def blog_pub(request):
    if request.method == 'GET':
        categories=Blogcategory.objects.all()
        return render(request,'blog_pub.html',context={'categories':categories})
    else:
        form=pubblogform(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            category_id=form.cleaned_data.get('category')
            Blog.objects.create(title=title,content=content,category=category_id,author=request.user)
            return JsonResponse({'code':200,'message':'博客发布成功'})
        else:
            print(form.errors)
            return JsonResponse({'code':404,'message':'博客发布失败'})
        