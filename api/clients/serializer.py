from rest_framework import serializers
from api.clients.models import Clients

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'