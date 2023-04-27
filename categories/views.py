from django.shortcuts import render
from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
