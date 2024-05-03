from rest_framework import serializers
from api.clients.models import Clients

class clientserializer():
    class meta:
        modul = Clients
        fields = '__all__'