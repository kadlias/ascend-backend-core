from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, NetworkConnection
from .serializers import UserSerializer, NetworkConnectionSerializer
class UserViewSet(viewsets.ReadOnlyModelViewSet): queryset=CustomUser.objects.all(); serializer_class=UserSerializer; permission_classes=[IsAuthenticated]
class NetworkConnectionViewSet(viewsets.ModelViewSet):
    serializer_class=NetworkConnectionSerializer; permission_classes=[IsAuthenticated]
    def get_queryset(self): return NetworkConnection.objects.filter(requester=self.request.user) | NetworkConnection.objects.filter(receiver=self.request.user)
    def perform_create(self, serializer): serializer.save(requester=self.request.user)
