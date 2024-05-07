from rest_framework import viewsets,mixins
from api.clients.serializer import ClientSerializer
from api.clients.models import Clients

class ClientGenericViewSet( mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    
    serializer_class = ClientSerializer
    queryset = Clients.objects.all()

