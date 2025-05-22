from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from .models import Application


User = get_user_model()


class ApplicationSubmitViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('application-submit')  # Update with your URL name
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '+1234567890',
            'resume': SimpleUploadedFile("resume.pdf", b"file_content", content_type="application/pdf")
        }

    @patch('account.tasks.send_email_to_applicant.delay')
    @patch('account.tasks.send_email_to_attorneys.delay')
    def test_create_application_unauthenticated(self):
        """Allow any unauthenticated user to submit"""
        response = self.client.post(self.url, self.valid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 1)

    def test_missing_required_fields(self):
        """Test validation for required fields"""
        invalid_data = self.valid_data.copy()
        del invalid_data['first_name']
        response = self.client.post(self.url, invalid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)

    def test_invalid_file_format(self):
        """Test file validation"""
        invalid_data = self.valid_data.copy()
        invalid_data['resume'] = SimpleUploadedFile("resume.png", b"file_content", content_type="text/plain")
        response = self.client.post(self.url, invalid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)



class ApplicationListViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('list')  # Update with your URL name
        self.user = User.objects.create_user(
            username='attorney',
            password='testpass',
            role='attorney'
        )
        self.non_attorney = User.objects.create_user(
            username='client',
            password='testpass'
        )
        self.app1 = Application.objects.create(first_name='John', last_name='Doe', email='john@example.com')
        self.app2 = Application.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com')

    def test_list_applications_authenticated_attorney(self):
        """Attorney can see all applications"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_applications_unauthenticated(self):
        """Unauthenticated users get 403"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_applications_non_attorney(self):
        """Non-attorney users get 403"""
        self.client.force_authenticate(user=self.non_attorney)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ordering(self):
        """Test applications are ordered by -id"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.data[0]['id'], self.app2.id)
        self.assertEqual(response.data[1]['id'], self.app1.id)


class ApplicationUpdateViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='attorney',
            password='testpass',
            role='attorney'
        )
        self.non_attorney = User.objects.create_user(
            username='client',
            password='testpass'
        )
        self.application = Application.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            status='pending'
        )
        self.url = reverse('detail', kwargs={'pk': self.application.pk})
        self.valid_data = {
            'status': 'reached_out'
        }

    def test_update_application_authenticated_attorney(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.application.refresh_from_db()
        self.assertEqual(self.application.status, 'reached_out')

    def test_update_application_unauthenticated(self):
        """Unauthenticated users get 403"""
        response = self.client.patch(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_application_non_attorney(self):
        """Non-attorney users get 403"""
        self.client.force_authenticate(user=self.non_attorney)
        response = self.client.patch(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_status_update(self):
        """Test validation for status field"""
        self.client.force_authenticate(user=self.user)
        invalid_data = self.valid_data.copy()
        invalid_data['status'] = 'pending'
        response = self.client.patch(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)