
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "discount",
            "stock",
            "final_price",
            "in_stock",
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    def validate_discount(self, value):
        if value < 0:
            raise serializers.ValidationError("Discount cannot be negative.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def validate(self, data):
        if data["discount"] > data["price"]:
            raise serializers.ValidationError(
                "Discount cannot be greater than price."
            )
        return data

    def get_final_price(self, obj):
        return obj.price - obj.discount

    def get_in_stock(self, obj):
        return obj.stock > 0