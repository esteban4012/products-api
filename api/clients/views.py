from rest_framework import viewsets
from api.clients.seralizer import clientserializer
from api.clients.models import Clients

class clientview():
    serialezer_class = clientserializer
    queryset = Clients.objects.all()

