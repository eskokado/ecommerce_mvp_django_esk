from django.urls import path

from orders.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("orders/", OrderListCreateAPIView.as_view(), name="orders-list-create"),
    path("orders/<int:pk>/", OrderRetrieveUpdateDestroyAPIView.as_view(), name="orders-retrieve-update-destroy"),
]
