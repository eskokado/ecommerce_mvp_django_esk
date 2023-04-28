from rest_framework import generics

from carts.models import Cart
from carts.serializers import CartSerializer
from django.contrib.auth.models import User


class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        user = User.objects.get(pk=user_id)
        serializer.save(user=user)


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
