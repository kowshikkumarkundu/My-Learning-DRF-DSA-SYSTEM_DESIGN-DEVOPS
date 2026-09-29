from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
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