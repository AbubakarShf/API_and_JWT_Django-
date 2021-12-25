from functools import partial
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import response
from django.shortcuts import render
from .Serializer import StudentSerializer, UserSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken,OutstandingToken,BlacklistedToken



class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        # token_obj,_=Token.objects.get_or_create(user=user)
        return Response({"status":200,"payload": serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),"Message":"You send this!"})

class LogoutUser(APIView):
    def post(self,request):
        response=Response()
        Flag=response.delete_cookie('jwt')
        print(Flag)
        return Response({
            'message':"User Logout Successfully!"
        })
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(id=request.data['id'])
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)
        print(t)
        return Response({messages:"lOGOUT ALL DONE"})

class StudentAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        student_Obj=Student.objects.all()
        serializer=StudentSerializer(student_Obj,many=True)
        return Response({"status":200,"payload": serializer.data})

    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=request.data)
        data=serializer.validate(data)
        if not serializer.is_valid():
            return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
        else:
            serializer.save()
            return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})

    def put(self,request):
        try:
            student_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student_obj,data=request.data,partial=False)
            if not serializer.is_valid():
                return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
            else:
                serializer.save()
                return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})
        except Exception as e:
            return Response({"Status":403,"Message":"ID not found"})

    def patch(self,request):
        try:
            student_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
            else:
                serializer.save()
                return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})
        except Exception as e:
            return Response({"Status":403,"Message":"ID not found"})

    def delete(self,request):
        try:
            id=request.GET.get('id')
            student_obj=Student.objects.get(id=id)
            student_obj.delete()
            return Response({"Status":200,"Message":"Delete Successfully"})

        except Exception as e:
            return Response({"Status":403,"Message":"ID not found"})

















# @api_view(['GET'])
# def home(request):
#     student_Obj=Student.objects.all()
#     serializer=StudentSerializer(student_Obj,many=True)
#     return Response({"status":200,"payload": serializer.data})


# @api_view(['POST'])
# def student_post(request):
#     data=request.data
#     serializer=StudentSerializer(data=request.data)
#     data=serializer.validate(data)
#     if not serializer.is_valid():
#         return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
#     else:

#         serializer.save()
#         return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})


# @api_view(['PUT'])
# def student_put(request,id):
#     try:
#         student_obj=Student.objects.get(id=id)
#         serializer=StudentSerializer(student_obj,data=request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
#         else:
#             serializer.save()
#             return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})
#     except Exception as e:
#         return Response({"Status":403,"Message":"ID not found"})

# @api_view(['DELETE'])
# def student_delete(request,id):
#     try:
#         student_obj=Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({"Status":200,"Message":"Delete Successfully"})

#     except Exception as e:
#         return Response({"Status":403,"Message":"ID not found"})
