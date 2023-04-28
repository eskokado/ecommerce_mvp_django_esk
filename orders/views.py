from rest_framework import generics
from django.contrib.auth.models import User
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        if user_id:
            user = User.objects.get(pk=user_id)
            serializer.save(user=user)
