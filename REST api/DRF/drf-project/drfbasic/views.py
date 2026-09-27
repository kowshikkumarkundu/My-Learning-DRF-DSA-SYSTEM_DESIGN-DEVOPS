from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# @api_view(['GET'])
# def product_list(request):

#     category = request.query_params.get("category")
    
#     return Response({
#     "message": "Products fetched",
#     "category": category
# })

# GET /api/products/?category=electronics&page=2

# Class Based View

class ProductList(APIView):
    def get(self,request):
        return Response({
    "message": "Product list"
})

    def post(self,request):

        name = request.data.get("name")
        price = request.data.get("price")

        return Response({
            "name": name,
            "price": price
        })

class ProductDetails(APIView):
    
    def get(self,request,pk):
        return Response({
            "product_id": pk
        })


