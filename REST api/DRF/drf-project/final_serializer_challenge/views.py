from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status
from .models import Product

class ProductView(APIView):
    def get(self,request):

        user_data = Product.objects.all()

        serialize = ProductSerializer(user_data,many=True)

        return Response(serialize.data)

    def post(self,request):

        products = request.data

        serializer = ProductSerializer(data=products)

        serializer.is_valid(raise_exception=True)

        product = serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )