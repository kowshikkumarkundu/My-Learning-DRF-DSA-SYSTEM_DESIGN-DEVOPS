from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    is_stock = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    discount = serializers.IntegerField(default=0)
    stock = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'discount',
            'stock',
            'is_stock',
            'final_price'
        ]

    def validate_price(self,value):
        if value < 0:
            return "price can't be Negative"
        return value

    def validate_discount(self,value):
        if value < 0:
            return "discount can't be Negative"
        return value

    def validate_stock(self,value):
        if value < 0:
            return "stock can't be Negative"
        return value

    def get_is_stock(self,obj):
        return obj.stock > 0

    def get_final_price(self,obj):
        return obj.price - obj.discount
    
    
