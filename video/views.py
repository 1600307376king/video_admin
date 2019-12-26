from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # 添加两个变量，并给它们赋值
    site_name = 'Django中文网'
    url = 'www.django.cn'
    # 把两个变量封装到上下文里
    context = {
        'site_name': site_name,
        'url': url,
    }
    # 把上下文传递到模板里
    return render(request, 'login.html', context)

