from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItem, Product, Collection, Review
from .serializers import ProductSerializer, CollectionsSerializer, ReviewSerializer
from django.db.models import Count
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


class ReviewApiViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def get(self, request):
    #     products = Product.objects.select_related("collection").all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


# function base view
# @api_view(['GET', "POST"])
# def product_list_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_fields = ["collection_id", "price"]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination
    search_fields = ["title", "description"]
    ordering_fields = ["price", "last_update"]

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ProductDetailApiView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitem.set.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
def product_detail_api_view(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionApiViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(proudcts_count=Count("product")), pk=pk
        )

        if collection.objects.acount() > 0:
            return Response(
                {
                    "error": "Collection cannot be deleted.because it is included one or more produts."
                }
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class base view
class CollectionApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Collection.objects.annotate(proudcts_count=Count("product")).all()
        serializer = CollectionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CollectionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Function base view
# @api_view(['POST',"GET"])
# def collection_api_list_view(request):
#     # collection = get_object_or_404(Collection.objects.annotate(proudcts_count= Count('products')), pk=pk)
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(proudcts_count= Count('product')).all()
#         serializer = CollectionsSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionDetailApiView(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(proudcts_count=Count("product")), pk=pk
        )
        serializer = CollectionsSerializer(collection)
        return Response(serializer.data)

    def post(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(proudcts_count=Count("product")), pk=pk
        )
        serializer = CollectionsSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(proudcts_count=Count("product")), pk=pk
        )

        if collection.objects.acount() > 0:
            return Response(
                {
                    "error": "Collection cannot be deleted.because it is included one or more produts."
                }
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def collection_detail_api_view(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(proudcts_count=Count("product")), pk=pk
    )

    if request.method == "GET":
        serializer = CollectionsSerializer(collection)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CollectionsSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        if collection.objects.acount() > 0:
            return Response(
                {
                    "error": "Collection cannot be deleted.because it is included one or more produts."
                }
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionApiView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Collection.objects.all()

    def get_serializer_class(self):
        return CollectionsSerializer


class ReivewApiViewSet(ModelViewSet):
    def get_queryset(self):
        return Review.objects.all()

    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
