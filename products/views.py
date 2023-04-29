from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated


class ProductListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
