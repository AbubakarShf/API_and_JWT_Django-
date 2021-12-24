from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('',views.home,name="home"),
    path('student_post',views.student_post,name="student_post"),
    path('student_put/<id>/',views.student_put,name="student_put"),
    path('student_delete/<id>/',views.student_delete,name="student_delete")
]