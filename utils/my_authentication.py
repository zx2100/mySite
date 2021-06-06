from django_redis import get_redis_connection
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt


class MyAuthentication(JSONWebTokenAuthentication):

    def __init__(self):
        self.request = None

    def authenticate(self, request):
        self.request = request
        token = self.get_head("Authorization")
        if not token:
            raise NotAuthenticated('未通过认证')
        # 验证请求头token是否过期
        try:
            payload = self.jwt_decode_token(token)
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('签名过期')
        except jwt.DecodeError:
            raise AuthenticationFailed('解码失败')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('非法用户')
        user = self.authenticate_credentials(payload)

        # 连接redis，判断是否存在对应KEY
        redis = get_redis_connection('default')
        if redis.exists(token) == 0:
            raise AuthenticationFailed('签名过期')

        return user, token


    def get_head(self, head):
        return self.request.META.get("%s" % ("HTTP_" + head.upper()))