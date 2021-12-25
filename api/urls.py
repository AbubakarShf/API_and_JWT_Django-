from django.contrib import admin
from django.urls import path,include
from api import views
from .views import StudentAPI,RegisterUser
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # path('',views.home,name="home"),
    # path('student_post',views.student_post,name="student_post"),
    # path('student_put/<id>/',views.student_put,name="student_put"),
    # path('student_delete/<id>/',views.student_delete,name="student_delete")

    path('student/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]