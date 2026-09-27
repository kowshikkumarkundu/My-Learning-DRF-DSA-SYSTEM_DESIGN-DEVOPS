from rest_framework import serializers
from .models import Author,Book

# without using Models
# ------------------------
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     price = serializers.IntegerField()
#     discount = serializers.IntegerField()

#     #field level validation
#     def validate_price(self,value):
#         if value < 0:
#             raise serializers.ValidationError(
#                 "price can't be negative"
#             )
#         return value
#     def validate_discount(self,value):
#         if value < 0:
#             raise serializers.ValidationError(
#                 "Discount price can't be negative"
#             )
#         return value

#     #object level validation
#     def validate(self, attrs):
#         if attrs["discount"] > attrs["price"]:
#             raise serializers.ValidationError(
#                 "Discount cannot be greater than price."
#             )

#         return attrs

#     def create(self,validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get(
#             "name",
#             instance.name
#         )
#         instance.price = validated_data.get(
#             "price",
#             instance.price
#         )

#         instance.save()
#         return instance


# Using Models
# ----------------------

# class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)
    # password = serializers.CharField(write_only = True)
    # discount = serializers.IntegerField(default=0)
    # cost_price = serializers.IntegerField(write_only=True)
    
    # class Meta:
    #     model = Product
    #     fields = ['id','username','password','name','price','discount','cost_price']

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Author
        fields = ['name','books']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all()
    )
    class Meta:
        model = Book
        fields = ['id','title','price','author']