from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import status
# Create your views here.
from .models import *
# from .serializers import ArticleGetSerializers, ArticlePostSerializers
from rest_framework.views import APIView
from utils.MyResponse import MyResponse
from utils.getUser import TokenGetUser
import datetime

class GetALLView(APIView):
    permission_classes = []

    #获取文章
    # def get(self, request):
    #     query_set = ArticlePost.objects.all()
    #     result = ArticleGetSerializers(query_set, many=True)
    #     # print(result)
    #     result = MyResponse(data=result.data, code=status.HTTP_200_OK, msg="获取成功")
    #     return result

    # 保存文章


class PostArticle(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # print(request.headers['Authorization'])

        # 刚开始打算数据导入到mysql中，但不够灵活，所以换成mongodb了
        # serializer = ArticlePostSerializers(data=request.data)
        # if serializer.is_valid():
        #     print("验证通过")
        #     serializer.save()
        #     print(serializer.data)
        # else:
        #     print(serializer.errors)

        # return Response(serializer.errors)

        # 文章保存在mongodb中

        # result = connect('one',
        #                  alias="mongodb",
        #                  host='172.81.215.108:27017',
        #                  port=27017,
        #                  username="admin",
        #                  password="Shell523569!")
        #
        # print(result)
        # 保存文章到mongodb
        # post = Articles()
        # # 对数据的一系列判断
        # post.author = "test"
        # post.brief = "xxxx"
        # post.category = "xxx"
        # post.title = "谢谢谢谢"
        # post.content = "xxxxssda"
        # # post.updated = "xxxx"
        # result = post.save()
        # print(result._data)
        # post = Post()
        # post.create(request.data)
        # print(post.save())

        # 获取用户
        user = TokenGetUser(request.headers.get('Authorization')).info()

        # 新建文章对象
        new_post = Post()
        new_post.create(data=request.data, user=user['uname'])
        new_post.save()
        return HttpResponse("xxx")


class Post:
    def __init__(self, *args, **kwargs):

        self.post = ""

    def create(self, data, user):
        att = data['data']
        self.post = Articles()
        self.post.author = user
        self.post.brief = att["brief"]
        self.post.category = att["category"]
        self.post.title = att["title"]
        self.post.content = att["content"]
        self.post.created = datetime.datetime.now()

    def save(self):
        if self.post:
            return self.post.save()


