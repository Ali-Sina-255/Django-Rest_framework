from django.contrib import admin
from . models  import Product, Collection, Promotion

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Promotion)