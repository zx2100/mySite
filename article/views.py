from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import status
# Create your views here.
from .models import *
from .serializers import ArticlePostSerializers
from rest_framework.views import APIView


class GetALLView(APIView):
    permission_classes = []

    #获取文章
    def get(self, request):
        query_set = ArticlePost.objects.all()
        result = ArticlePostSerializers(query_set, many=True)
        # print(result)
        result = Response(result.data, status=status.HTTP_200_OK)
        return result

    # 保存文章
    def post(self, request):
        print(request.data)

        # result = Response({"xx": "xx"}, status=status.HTTP_200_OK)
        return HttpResponse("xx11")
