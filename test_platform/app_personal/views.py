from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# 请求处理逻辑


def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, 'login.html', {'error': ''})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "" or password == "":
            return render(request, 'login.html', {'error': '用户名或密码为空'})
        user = auth.authenticate(username=username, password=password)  # 用户名和密码不正确返回None
        if user is not None:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'login.html', {'error': '账号或密码错误'})
    else:
        print('shabi')


@login_required()
def index(request):
    '''
    主页
    :param request:
    :return:
    '''
    return render(request, "index.html")


def logout(request):
    '''
    注销
    :return:
    '''
    auth.logout(request)
    return HttpResponseRedirect('/')