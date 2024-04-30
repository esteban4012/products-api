from rest_framework import viewsets
from .serializer import ProductSerializer
from api.products.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()