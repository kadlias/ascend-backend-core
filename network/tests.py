from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser, NetworkConnection

class NetworkModelTests(TestCase):
    def test_connection_defaults_to_pending(self):
        first = CustomUser.objects.create_user(username='first', email='first@example.com', password='safe-password')
        second = CustomUser.objects.create_user(username='second', email='second@example.com', password='safe-password')
        connection = NetworkConnection.objects.create(requester=first, receiver=second)
        self.assertEqual(connection.status, NetworkConnection.PENDING)

    def test_authenticated_user_can_create_and_list_connections(self):
        first = CustomUser.objects.create_user(username='first', email='first@example.com', password='safe-password')
        second = CustomUser.objects.create_user(username='second', email='second@example.com', password='safe-password')
        client = APIClient(); client.force_authenticate(first)
        response = client.post('/api/connections/', {'receiver': second.id}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(client.get('/api/connections/').data[0]['receiver'], second.id)

# Create your tests here.
