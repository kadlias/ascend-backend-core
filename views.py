from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, NetworkConnection
from .serializers import UserSerializer, NetworkConnectionSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint para listar y ver detalles de usuarios en la red.
    Solo lectura para proteger la integridad de los usuarios.
    """
    # select_related optimiza la consulta SQL haciendo un JOIN en base de datos
    queryset = CustomUser.objects.select_related('profile').all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class NetworkConnectionViewSet(viewsets.ModelViewSet):
    """
    Gestión completa de invitaciones y conexiones en la red ASCEND.
    """
    serializer_class = NetworkConnectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtro de seguridad: El usuario autenticado solo puede ver 
        las conexiones donde él es el remitente o el receptor.
        """
        user = self.request.user
        return NetworkConnection.objects.filter(requester=user) | NetworkConnection.objects.filter(receiver=user)

    def perform_create(self, serializer):
        """
        Al crear una solicitud, el backend asigna automáticamente 
        al remitente basándose en el token de autenticación.
        """
        serializer.save(requester=self.request.user)

    @action(detail=True, methods=['post'])
    def accept_request(self, request, pk=None):
        """
        Lógica de negocio personalizada para aceptar una conexión.
        Se accede vía POST: /api/connections/{id}/accept_request/
        """
        connection = self.get_object()
        
        # Validaciones de seguridad
        if connection.receiver != request.user:
            return Response({"detail": "No tienes permiso para aceptar esta solicitud."}, status=status.HTTP_403_FORBIDDEN)
            
        if connection.status != 'PENDING':
            return Response({"detail": "Esta solicitud ya fue procesada anteriormente."}, status=status.HTTP_400_BAD_REQUEST)

        # Actualización de estado que mencionamos en el README
        connection.status = 'ACCEPTED'
        connection.save()
        return Response({"status": "Conexión aceptada exitosamente."}, status=status.HTTP_200_OK)
