from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class NetworkConnection(models.Model):
    PENDING, ACCEPTED, BLOCKED = 'PENDING', 'ACCEPTED', 'BLOCKED'
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=[(PENDING, 'Pending'), (ACCEPTED, 'Accepted'), (BLOCKED, 'Blocked')], default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: constraints = [models.UniqueConstraint(fields=['requester','receiver'], name='unique_connection')]
