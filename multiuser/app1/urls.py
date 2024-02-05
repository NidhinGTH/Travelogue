# your_app/urls.py

from django.urls import path
from app1 import views

app_name = "app1"

urlpatterns = [
    path('', views.home, name="home"),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('teachersignup', views.teachersignup, name='teachersignup'),
    path('adminhome', views.adminhome, name="adminhome"),
    path('studenthome', views.studenthome, name="studenthome"),
    path('teacherhome', views.teacherhome, name="teacherhome"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('userlogout', views.user_logout, name="userlogout")
]


