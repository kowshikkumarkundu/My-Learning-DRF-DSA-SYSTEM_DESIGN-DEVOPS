from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()

        serializer = ProductSerializer(products,many=True)

        return Response(
            serializer.data
        )

    def post(self,request):
        
        serializer = ProductSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)

        product = serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class ProductDetail(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)

        serializer = ProductSerializer(product)

        return Response(
            serializer.data
        )
    def put(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(
            instance = product,
            data = request.data
        )

        serializer.is_valid(raise_exception=True)

        product = serializer.save()

        return Response(
            serializer.data,
        )

    def patch(self,request,pk):
            
        product = get_object_or_404(Product,pk=pk)

        serializer = ProductSerializer(
            instance = product,
            data = request.data,
            partial = True
        )

        serializer.is_valid(raise_exception=True)

        product = serializer.save()

        return Response(
            serializer.data,
        )

    
    def delete(self,request,pk):
        product = get_object_or_404(Product,pk=pk)

        product.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )