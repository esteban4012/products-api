from django.db import models
from api.clients.models import Clients
from api.products.models import Product

class Order(models.Model):
    client_order = models.ForeignKey(Clients, on_delete=models.CASCADE)
    Product_order = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

   
