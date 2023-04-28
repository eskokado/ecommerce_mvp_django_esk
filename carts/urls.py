from django.urls import path

from carts.views import CartListCreateAPIView, CartRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("carts/", CartListCreateAPIView.as_view(), name="carts-list-create"),
    path("carts/<int:pk>/", CartRetrieveUpdateDestroyAPIView.as_view(), name="carts-retrieve-update-destroy"),
]
