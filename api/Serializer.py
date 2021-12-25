from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        # fields=['Name','Age']
        #OR
        # exclude=['FatherName']
        #OR
        fields='__all__'

    def validate(self,data):
        if data['Age']<18:
            raise serializers.ValidationError({"Error":"Age should be greater than 18."})
        if data['Name']:
            for n in data['Name']:
                if n.isdigit():
                    raise serializers.ValidationError({"Error":"Name shouldn't contain digits"})

        return data