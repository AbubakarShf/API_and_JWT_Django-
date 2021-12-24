from functools import partial
from django.shortcuts import render
from .Serializer import StudentSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    student_Obj=Student.objects.all()
    serializer=StudentSerializer(student_Obj,many=True)
    return Response({"status":200,"payload": serializer.data})


@api_view(['POST'])
def student_post(request):
    data=request.data
    serializer=StudentSerializer(data=request.data)
    data=serializer.validate(data)
    if not serializer.is_valid():
        return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
    else:

        serializer.save()
        return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})


@api_view(['PUT'])
def student_put(request,id):
    try:
        student_obj=Student.objects.get(id=id)
        serializer=StudentSerializer(student_obj,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({"status":403,"Errors":serializer.errors,"Message":"Something went wrong!"})
        else:
            serializer.save()
            return Response({"status":200,"payload": serializer.data,"Message":"You send this!"})
    except Exception as e:
        return Response({"Status":403,"Message":"ID not found"})

@api_view(['DELETE'])
def student_delete(request,id):
    try:
        student_obj=Student.objects.get(id=id)
        student_obj.delete()
        return Response({"Status":200,"Message":"Delete Successfully"})

    except Exception as e:
        return Response({"Status":403,"Message":"ID not found"})