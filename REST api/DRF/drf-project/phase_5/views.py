from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):

        if self.action == "list":
            return Product.objects.all()

        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    @action(
        detail=False,
        methods=["get"]
    )
    def out_of_stock(self, request):

        products = Product.objects.filter(stock=0)

        serializer = self.get_serializer(
            products,
            many=True
        )

        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"]
    )
    def discount(self, request, pk=None):

        product = self.get_object()

        product.price -= 100
        product.save()

        return Response({
            "message": "Discount applied",
            "price": product.price
        })