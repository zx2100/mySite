# codeing:utf-8
from django.urls import path, re_path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('auth', AuthView.as_view()),
    path('profile', UserProfileView.as_view()),
    path('profile/<int:pk>', UserProfileDetailView.as_view()),
    path('test', Test.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
