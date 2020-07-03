# codeing:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *
import json
from django.core.serializers import serialize
#  使用django自带的认证
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def get_user_view(request):
    result = {
        "status": "400",
        "result": "Not Found"
    }
    if request.GET:
        try:
            user = request.GET['user']
        except Exception as e:

            result["result"] = "参数错误"
        else:
            #  返回查询对象
            query_set = UserProfile.objects.filter(username=user)
            # 判断是否找到
            if query_set:
                # 序列化Json,返回指定数据
                json_data = json.loads(serialize('json', query_set, fields=(
                    'last_login',
                    'username',
                    "email",
                    "date_joined",
                    "birthday",
                    "gender",
                    "phone_number",
                    "is_vip"
                )))
                # 只返回fields字段内容
                result['result'] = json_data[0]["fields"]
                result['status'] = "200"
    return JsonResponse(result)


def login_view(request):
    """处理登录"""
    result = {
        "status": "400",
        "result": "缺少必要参数"
    }

    # 检查参数
    if request.POST:
        try:
            username = request.POST["username"]
            passwd = request.POST["passwd"]
        except Exception as e:
            result["result"] = "参数错误"
        else:
            # 登录验证
            user = authenticate(username=username, password=passwd)
            if user is not None:
                # 加入login会话中，加入后，会返回cookies
                login(request, user)
                result = {
                    "status": "200",
                    "result": "验证通过"
                }
                print(request.user.is_authenticated)
            else:
                result = {
                    "status": "201",
                    "result": "验证失败"
                }
    return JsonResponse(result)


@login_required
def logout_view(request):
    # 登出绘画
    logout(request)
    return HttpResponse("ok")


def login_redirect_view(request):
    result = {
        "status": "400",
        "result": "error"
    }
    if request.GET:
        result = {
            "status": "302",
            "result": "未通过验证"
        }
    return JsonResponse(result)
