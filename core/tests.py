from django.test import SimpleTestCase
from django.urls import reverse


class AuthenticationRoutesTests(SimpleTestCase):
    def test_password_reset_confirm_route_exists(self):
        url = reverse('password_reset_confirm', kwargs={'uidb64': 'test', 'token': 'token'})
        self.assertEqual(url, '/password-reset-confirm/test/token/')

    def test_password_reset_complete_route_exists(self):
        url = reverse('password_reset_complete')
        self.assertEqual(url, '/password-reset-complete/')

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/?next=/dashboard/', response['Location'])
