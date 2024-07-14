from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListApiView.as_view(),name='product-list'),
    path('<int:pk>/', views.ProductDetailApiView.as_view(),name='product-detail'),
    path('collections/', views.CollectionApiView.as_view(),name='collection'),
    path('collections/<int:pk>/', views.CollectionDetailApiView.as_view(),name='collection-detail'),
]
