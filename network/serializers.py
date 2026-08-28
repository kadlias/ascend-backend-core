from rest_framework import serializers
from .models import CustomUser, NetworkConnection
class UserSerializer(serializers.ModelSerializer):
    class Meta: model = CustomUser; fields = ['id','username','email','is_verified']
class NetworkConnectionSerializer(serializers.ModelSerializer):
    class Meta: model = NetworkConnection; fields = ['id','requester','receiver','status','created_at']; read_only_fields=['requester','status']
