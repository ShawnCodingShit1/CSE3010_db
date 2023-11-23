from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse


# 创建你的视图函数
def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    if request.method == 'POST':
        u = request.POST.get("username", '')
        p = request.POST.get("password", '')

        # 使用你的实际用户验证逻辑替换这个条件
        if u  and p :
            login_result = DoctorInfo.objects.filter(doctor_id=u, doctor_password=p).count()
            if login_result == 1:
                return HttpResponse("登录成功")
            else:
                return HttpResponse("账号密码错误")
        else:
            return HttpResponse("账号密码不能为空")
        

    return HttpResponse("无效请求")
#注册页面
def toRegister_view(request):
    return render(request, 'register.html')

#注册后的逻辑判断
def Register_view(request):
    u = request.POST.get("username", '')
    p = request.POST.get("password", '')
    if u and p:
        register_info = DoctorInfo(doctor_id=u, doctor_password=p)
        register_info.save()
        login_url = reverse('login')  # 获取登录页面URL
        return HttpResponse(f"register success! <a href='{login_url}'>返回登录页面</a>")
    else:
        return HttpResponse("register failed")