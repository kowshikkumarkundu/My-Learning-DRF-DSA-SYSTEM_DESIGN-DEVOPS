from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student

class StudentView(APIView):
    def get(self,request):
        student = Student.objects.all()

        serializer = StudentSerializer(student, many=True)

        return Response(
            serializer.data
        )

    def post(self,request):
        serializer = StudentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        student = serializer.save()

        return Response(
            StudentSerializer(student).data,
            status=status.HTTP_201_CREATED
        )