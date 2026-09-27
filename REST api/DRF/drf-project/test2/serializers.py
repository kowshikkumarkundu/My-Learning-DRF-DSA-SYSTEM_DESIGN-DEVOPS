from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    grade = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['name','age','marks','grade']

    def validate_marks(self,mark):
        if mark < 0:
            raise serializers.ValidationError(
                "marks can't be negative"
            )
        if mark > 100:
            raise serializers.ValidationError(
                "Marks can't more than 100"
            )
        return mark

    def validate_age(self,age):
        if age<0:
            raise serializers.ValidationError(
                "age can't be negative"
            )
        return age

    def grade_calculate(self,mark):
        if mark>=80:
            return "A"
        elif mark>=60:
            return "B"
        elif mark>=40:
            return "C"
        else:
            return "F"
        
    def get_grade(self,obj):
        return self.grade_calculate(obj.marks)
