from rest_framework import serializers
from .models import *

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