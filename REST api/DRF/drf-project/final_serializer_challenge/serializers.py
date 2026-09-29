from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()
    discount = serializers.IntegerField(default=0)
    stock = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ['id','name','price','discount','stock','final_price','in_stock']

    def validate_price(self,price):
        if price<0:
            raise serializers.ValidationError(
                "Price can't be less than 0"
            )
        return price
    
    def validate_discount(self,discount):
        if discount < 0:
            raise serializers.ValidationError(
                "discount can't be less than 0"
            )
        return discount

    def validate_stock(self,value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock can't be less than 0"
            )
        return value

    def validate(self,data):
        if data['price'] < data['discount']:
            raise serializers.ValidationError(
                "discount can't be more than price"
            )
        return data
    
    def get_final_price(self,obj):
        return obj.price - obj.discount

    def get_in_stock(self,obj):
        return obj.stock>0