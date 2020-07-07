# codeing:utf-8
from .models import UserProfile
from django.http import HttpResponse
from .serializers import UserProfileSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.shortcuts import Http404
from rest_framework_jwt.settings import api_settings

# 这个试图不需要认证
class auth_view(APIView):
    def post(self, request):
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
        return Response({"success": True, "msg": "登录成功", "results": token}, status=status.HTTP_200_OK)

#     重新权限方法,这个视图不检查身份
    def get_permissions(self):
        return []


# 查看或创建用户
class UserProfileView(generics.ListCreateAPIView):
    # 配置认证信息
    def get(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializers(queryset, many=True)
        return Response(serializer.data)


class UserProfileDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
