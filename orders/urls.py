from django.urls import path

from orders.views import OrderListCreateAPIView

urlpatterns = [
    path("orders/", OrderListCreateAPIView.as_view(), name="orders-list-create"),
]
