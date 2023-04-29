from django.shortcuts import render
from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer
from users.permissions import IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedAndAdminOrSafeMethodsAndAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
