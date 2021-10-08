from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from study.models import study
from django.contrib.auth.models import User


def mypage(request):
    user = request.user
    my_study = study.objects.filter(study_member=user)
    my_study_request = study.objects.filter(study_member_request=user)
    return render(
        request,
        "mypage/mypage.html",
        {"my_study": my_study, "my_study_request": my_study_request},
    )
