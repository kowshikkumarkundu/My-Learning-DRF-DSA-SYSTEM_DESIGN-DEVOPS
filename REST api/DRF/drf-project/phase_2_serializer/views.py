from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorSerializer,BookSerializer
from .models import Author,Book

# class Product(APIView):

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             return Response(serializer.validated_data)

#         return Response(serializer.errors, status=400)

class BookCreateView(APIView):

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        book = serializer.save()

        return Response(
            BookSerializer(book).data,
            status=status.HTTP_201_CREATED
        )