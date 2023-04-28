from django.urls import path

from products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="products-list-create"),
    path("products/<int:pk>/", ProductRetrieveUpdateDestroyAPIView.as_view(), name="products-retrieve-update-destroy"),
]
