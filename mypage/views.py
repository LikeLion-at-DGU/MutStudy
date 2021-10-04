from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
# from main.models import # 글가져오기 
from django.contrib.auth.models import User

def mypage(request):
    user = request.user 
    #글가져오기
    return render(request,'mypage/mypage.html')