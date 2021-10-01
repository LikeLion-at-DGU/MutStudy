from django.urls import path
from main import views
from .views import *

app_name = "main"
urlpatterns = [
    path('', views.showmain, name="showmain"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('work-single/', views.worksingle, name="worksingle"),
    path('work/', views.work, name="work"),
]
