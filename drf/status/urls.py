from django.contrib import admin
from django.urls import path
# from updates.views import *
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import url
urlpatterns = [
    path('', StatusApiView.as_view()),
    # path('/create', StatusCreateAPIView.as_view()),
    path('detail/<int:id>', StatusDetailAPIView.as_view())
]

