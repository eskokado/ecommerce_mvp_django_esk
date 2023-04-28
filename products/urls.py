from django.urls import path

from products.views import ProductListCreateAPIView

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="products-list-create"),
]
