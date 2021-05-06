# codeing:utf-8
from .models import UserProfile
from .serializers import UserProfileSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import Http404
from rest_framework_jwt.settings import api_settings
from .permissions import OnlySuperAdmin
from rest_framework.permissions import IsAuthenticated
from utils.MyResponse import MyResponse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 这个视图不需要认证
class AuthView(APIView):
    # 不做权限检查
    permission_classes = []

    def post(self, request):
        # Bearer 认证通过后加上Bearer
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        print(user)
        # 认证通过
        if not user:
            raise Http404("账号密码不匹配")
        # login(request, user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        result = {
                "token": token,
                "username": user.username,
                "userid": user.id
        }

        result = MyResponse(data=result, msg="认证通过", code=status.HTTP_200_OK)
        return result


class TokenAuth:
    def authenticate(self, request):
        from rest_framework.exceptions import AuthenticationFailed
        from rest_framework_jwt.serializers import VerifyAuthTokenSerializer
        token = {"token": None}
        # print(request.META.get("HTTP_TOKEN"))
        token["token"] = request.META.get('HTTP_TOKEN')
        valid_data = VerifyAuthTokenSerializer().validate(token)
        print(valid_data)
        user = valid_data['user']
        print(user)
        if user:
            return
        else:
            from utils.Myexception import custom_exception_handler
            raise AuthenticationFailed('认证失败')

# 查看或创建用户
class UserProfileView(APIView):
    """
    只有超级管理员才能调用此视图
    """
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated, OnlySuperAdmin]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = UserProfile.objects.all()
    # 配置认证信息

    def get(self, request):
        serializer = UserProfileSerializers(self.queryset, many=True)
        return Response(serializer.data)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

