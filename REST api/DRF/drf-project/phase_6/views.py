from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BaseAuthentication

class HeaderAuthentication(BaseAuthentication):

    def authenticate(self, request):
        ...
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def who_am_i(self, request):
        return Response({
            "user": str(request.user),
            "auth": str(request.auth),
        })