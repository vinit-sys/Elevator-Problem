from rest_framework import serializers
from .models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('id', 'current_floor', 'destinations', 'status', 'direction', 'door')
