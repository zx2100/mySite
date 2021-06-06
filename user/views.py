# codeing:utf-8
from .models import UserProfile
from .serializers import UserProfileSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from .permissions import OnlySuperAdmin
from rest_framework.permissions import IsAuthenticated
from utils.my_response import MyResponse
from utils.my_tools import Token
# 导入自定义认证
from utils.my_exception import Unauthorized



# 这个视图不需要认证
class AuthView(APIView):
    # 不做权限检查
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        print(user)
        # 认证通过
        if not user:
            raise Unauthorized("账号或密码不匹配")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # print(jwt_payload_handler)
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        result = {
                "token": token,
                "username": user.username,
                "userid": user.id
        }
        from django_redis import get_redis_connection
        # 连接redis
        redis = get_redis_connection('default')
        # 保存redis数据
        redis.hmset(token, result)
        # 设置超时时间
        redis.expire(token, 60*60*24)
        result = MyResponse(data=result, msg="认证通过", code=status.HTTP_200_OK)
        return result



# 查看或创建用户
class UserProfileView(APIView):
    """
    只有超级管理员才能调用此视图
    """

    permission_classes = [IsAuthenticated]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # 配置认证信息

    def get(self, request):


        user = Token.get_user(request.headers["Authorization"])
        print(user)
        # 序列化数据
        queryset = UserProfile.objects.get(id=user['uid'])
        serializer = UserProfileSerializers(queryset)
        return Response(serializer.data)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class Test(APIView):

    # authentication_classes = (MyAuthentication, )
    # permission_classes = [IsAuthenticated]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):


        return MyResponse(data="其死亡")
