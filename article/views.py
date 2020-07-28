from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import status
# Create your views here.
from .models import *
from .serializers import ArticleGetSerializers, ArticlePostSerializers
from rest_framework.views import APIView
from utils.MyResponse import MyResponse


class GetALLView(APIView):
    permission_classes = []

    #获取文章
    def get(self, request):
        query_set = ArticlePost.objects.all()
        result = ArticleGetSerializers(query_set, many=True)
        # print(result)
        result = MyResponse(data=result.data, code=status.HTTP_200_OK, msg="获取成功")
        return result

    # 保存文章


class PostArticle(APIView):
    permission_classes = []

    def post(self, request):
        print(request.data)

        # 验证数据
        # serializer = ArticlePostSerializers(data=request.data)
        # if serializer.is_valid():
        #     print("验证通过")
        #     serializer.save()
        #     print(serializer.data)
        # else:
        #     print(serializer.errors)

        # return Response(serializer.errors)

        # 文章保存在mongodb中
        from mongoengine import connect
        result = connect('project',
                         alias="project",
                         host='172.81.215.108:27017',
                         port=27017,
                         username="admin",
                         password="Shell523569!",
                         authentication_source='one')

        print(result)
        return HttpResponse("xxx")