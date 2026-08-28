from django.test import TestCase
from .models import CustomUser, NetworkConnection

class NetworkModelTests(TestCase):
    def test_connection_defaults_to_pending(self):
        first = CustomUser.objects.create_user(username='first', email='first@example.com', password='safe-password')
        second = CustomUser.objects.create_user(username='second', email='second@example.com', password='safe-password')
        connection = NetworkConnection.objects.create(requester=first, receiver=second)
        self.assertEqual(connection.status, NetworkConnection.PENDING)

# Create your tests here.
