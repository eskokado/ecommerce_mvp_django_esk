from django.urls import path

from carts.views import CartListCreateAPIView

urlpatterns = [
    path("carts/", CartListCreateAPIView.as_view(), name="carts-list-create"),
]
