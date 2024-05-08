from rest_framework import  viewsets
from api.order.serializer import OrderSerializer
from api.order.models import Order

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()