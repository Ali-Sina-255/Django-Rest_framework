from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    pige_size = 4
