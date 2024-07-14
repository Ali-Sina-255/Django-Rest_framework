from rest_framework import serializers
from decimal import Decimal

from . models import Product, Collection,Promotion

    
class PromotionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Promotion
        fields = ["description", "discount"]
    
    # description = serializers.CharField()
    # discount = serializers.FloatField()
        
class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Product
        fields = ['id','title','price','description','inventory','promotions']
    
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2)
    # price_with_txt = serializers.SerializerMethodField(method_name='calcuate_tax')
    # promotions = PromotionSerializer()

    def calcuate_tax(self, product:Product):
        return product.price * Decimal(1.1)
    

class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title', 'proudcts_count'] 
        
    proudcts_count = serializers.IntegerField(read_only=True)