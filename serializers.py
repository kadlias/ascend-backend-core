from rest_framework import serializers
from .models import CustomUser, UserProfile, NetworkConnection

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializador para los datos del perfil.
    """
    class Meta:
        model = UserProfile
        fields = ['bio', 'job_title', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador principal del usuario. 
    Incluye el perfil de forma anidada (nested) como solo lectura.
    """
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_verified', 'profile']

class NetworkConnectionSerializer(serializers.ModelSerializer):
    """
    Serializa las conexiones de red.
    Añade campos de solo lectura para traer los nombres de usuario directamente,
    evitando que el frontend tenga que hacer peticiones extra.
    """
    requester_username = serializers.CharField(source='requester.username', read_only=True)
    receiver_username = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = NetworkConnection
        fields = ['id', 'requester', 'requester_username', 'receiver', 'receiver_username', 'status', 'created_at']
        read_only_fields = ['status'] # El estado solo se cambia a través de endpoints específicos, no directamente.
