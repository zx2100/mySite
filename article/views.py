from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import status
# Create your views here.
from .models import *
# from .serializers import ArticleGetSerializers, ArticlePostSerializers
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
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

        # 获取用户
        user = TokenGetUser(request.headers.get('Authorization')).info()
        # 新建文章对象
        print(request.data)
        new_post = Post()
        new_post.create(data=request.data, user=user['uname'])
        return HttpResponse("xxx")


class Post:
    def __init__(self, *args, **kwargs):
        self.post = ""

    def create(self, data, user):
        """
        创建对象，成功返回True.失败返回False
        :param data:
        :param user:
        :return:
        """
        att = data.get('data')
        self.post = Articles()
        self.post.author = user
        self.post.brief = att.get("brief")
        # 判断分类是否合法
        if not self.has_category(att.get('category')):
            raise ParseError("文章分类有误")
        self.post.category = att.get("category")
        self.post.title = att.get("title")
        self.post.content = att["content"]
        self.post.created = datetime.datetime.now()

    def has_category(self, category):
        """
        判断分类是否合法
        :param category:
        :return:
        """
        print(category)
        return True if ArticleCategory.objects.filter(name=category).count() > 0 else False

    def save(self):
        if self.post:
            return self.post.save()
