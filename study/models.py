from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class study(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE) #작성자, User 모델 사용
    name = models.CharField(max_length=50) #스터디명
    section = models.CharField(max_length=30) #분야
    intro = models.CharField(max_length=100) #스터디 한줄 소개
    qualification = models.CharField(max_length=100) #스터디 참가 대상
    member_start = models.IntegerField(default=1) #모집 인원 시작 
    member_end = models.IntegerField(default=1) #모집 인원 끝
    start_date = models.DateTimeField() #활동 기간(시작일)
    due_date = models.DateTimeField() #활동 기간(마감일)
    body = models.TextField() #스터디 정보
    difficulty = models.IntegerField(default=0) #스터디 난이도(빡센 정도 1~10으로 입력받을 예정)
    phnum = models.CharField(max_length=13) #대표자 연락처
    image = models.FileField(
        upload_to="image/", null=True
    ) #스터디 관련 이미지(있으면 글 썸네일, 없으면 메인 로고가 글 썸네일)
    member = [] #가입자 명단(member id 들어올 예정)
    member_request = [] #가입 신청(member id 들어올 예정)