from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from backend.models import User


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            first_name='test_first_name',
            last_name='test_last_name',
            username='test_username'
        )
        user.set_password('test_password')
        user.save()

    def test_login_user_ok(self):
        client = APIClient()
        response = client.post(
            '/login/', {
                'username': 'test_username',
                'password': 'test_password',
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_login_user_ko(self):
        error_message = b'Please enter a correct username and password'
        client = APIClient()
        response = client.post(
            '/login/', {
                'username': 'bad_username',
                'password': 'other_password',

            },
            format='multipart'
        )
        self.assertIn(error_message, response.content)

    def test_update_user_ok(self):
        client = APIClient()
        client.login(username='test_username', password='test_password')
        response = client.put(
            '/api/user', {
                'name': 'new_name',
                'first_name': 'new_first_name',
                'email': 'new_email@email.com'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.first()
        self.assertEqual(user.name, 'new_name')

    def test_update_user_ko(self):
        client = APIClient()
        client.login(username='test_username', password='test_password')
        response = client.put(
            '/api/user', {
                'name': 'new_name',
                'first_name': 'new_first_name',
                'email': 'new_email'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user = User.objects.first()
        self.assertNotEqual(user.name, 'new_name')
