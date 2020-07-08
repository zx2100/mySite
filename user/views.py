# codeing:utf-8
from .models import UserProfile
from .serializers import UserProfileSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import Http404
from rest_framework_jwt.settings import api_settings
from .premissions import UserViewPremissions
from rest_framework.permissions import IsAuthenticated
import base64
import json


# 这个视图不需要认证
class AuthView(APIView):
    # 不做权限检查
    permission_classes = []
    def post(self, request):
        print("sada")
        user = authenticate(username=request.data["username"], password=request.data["password"])
        print(user)
        # 认证通过
        if not user:
            raise Http404("账号密码不匹配")
        # login(request, user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        result = Response({
            "success": True,
            "status": status.HTTP_200_OK,
            "msg": "登录成功",
            "results": token,
        }, status=status.HTTP_200_OK)
        return result


# 查看或创建用户
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated, UserViewPremissions]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = UserProfile.objects.all()
        self.user = {}
    # 配置认证信息
    def get(self, request):
        # 获取用户名
        # token = request.data['Authorization']
        # 获取token中的数据
        token_info = json.loads(base64.b64decode(request.headers["Authorization"].split(" ")[1].split(".")[1]+"=="))

        self.user = {
            "id": token_info['user_id'],
            "username": token_info['username']
        }
        serializer = UserProfileSerializers(self.queryset, many=True)
        return Response(serializer.data)



class UserProfileDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
