from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado para ASCEND.
    Extiende el AbstractUser de Django para futuras adaptaciones de autenticación.
    """
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    """
    Perfil detallado del usuario (Relación 1:1).
    Demuestra diseño de esquemas y separación de responsabilidades.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ascend_user_profiles'
        ordering = ['-created_at']

    def __str__(self):
        return f"Perfil de {self.user.username}"

class NetworkConnection(models.Model):
    """
    Gestión de la red privada (Relación Muchos a Muchos con atributos).
    Maneja el estado de las invitaciones entre usuarios.
    """
    STATUS_CHOICES = (
        ('PENDING', 'Pendiente'),
        ('ACCEPTED', 'Aceptada'),
        ('BLOCKED', 'Bloqueado'),
    )

    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ascend_network_connections'
        unique_together = ('requester', 'receiver') # Evita solicitudes duplicadas
        
    def __str__(self):
        return f"{self.requester} -> {self.receiver} ({self.status})"
