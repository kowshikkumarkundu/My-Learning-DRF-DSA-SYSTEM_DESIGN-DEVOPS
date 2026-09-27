from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Products(APIView):
    def get(self,request):
       category = request.query_params.get("category")

       if category:
            return Response({
                "message": "Products fetched",
                "category": category
            })
       return Response({
            "message": "Product list"
        })

    def post(self,request):

        name = request.data.get("name")
        price = request.data.get("price")

        return Response({
            "name": name,
            "price": price
        },
            status=status.HTTP_201_CREATED
        )

class ProductDetail(APIView):
    def get(self,request,pk):

        return Response(
            {
                "product_id": pk,
                "message": "Product details"
            }       
        )

# C. Short explanation

# request.data কী? => client je data provide kore post request e setai request.data 
# request.query_params কী? => client data fiilter korar jonno url e ? er pore ja jog kore setai query_param. like: api/product/?category=electronics
# pk কোথা থেকে আসে? => pk ase query params theke. ba je user request  korce tar id  
# POST-এর ক্ষেত্রে 201 কেন ব্যবহার করেছ? => 201 data create korche... data create success bujhate 201 response pathacche 
# APIView কীভাবে GET আর POST আলাদা করে? get request pathale Products.get, post request pathale Products.post call hoi

# GET  /products/ => get method
# GET  /products/?category=electronics => get method where category is electronics
# POST /products/ =>post method
# GET  /products/7/ => get method ,pk=7