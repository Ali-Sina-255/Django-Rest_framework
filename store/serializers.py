from rest_framework import serializers
from decimal import Decimal

from .models import Product, Collection, Promotion, Review, Cart, CartItem


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["description", "discount"]

    # description = serializers.CharField()
    # discount = serializers.FloatField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "description", "inventory", "promotions"]

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2)
    # price_with_txt = serializers.SerializerMethodField(method_name='calcuate_tax')
    # promotions = PromotionSerializer()

    def calcuate_tax(self, product: Product):
        return product.price * Decimal(1.1)


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "proudcts_count"]

    proudcts_count = serializers.IntegerField(read_only=True)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description", "date"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "items"]
