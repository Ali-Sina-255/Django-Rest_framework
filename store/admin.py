from django.contrib import admin
from .models import Product, Collection, Promotion, Cart, CartItem

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Promotion)
admin.site.register(Cart)
admin.site.register(CartItem)
