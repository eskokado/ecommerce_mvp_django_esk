from django.urls import path

from categories.views import CategoryListCreateAPIView

urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view(), name="categories")
]
