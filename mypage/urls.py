from django.urls import path
from . import views 
from .views import *

app_name = "mypage"
urlpatterns = [
    path('mypage/',views.mypage,name='mypage')
]
