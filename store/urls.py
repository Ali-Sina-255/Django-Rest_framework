from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("products", views.ProductApiViewSet, basename="products")
router.register("collections", views.CollectionApiViewSet)
router.register("cart", views.CartApiViewSet)

product_routers = routers.NestedDefaultRouter(router, "products", lookup="product")
product_routers.register("reviews", views.ReivewApiViewSet, basename="product-review")

urlpatterns = router.urls + product_routers.urls
