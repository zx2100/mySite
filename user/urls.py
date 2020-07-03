# codeing:utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path(r'login', login_view),
    path(r'logout', logout_view),
    path(r'get/', get_user_view),
    path(r'redirect', login_redirect_view)

]
