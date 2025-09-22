# users/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User



class LogoutTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testuserpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_logout(self):
        # Login qilamiz
        self.client.login(username=self.username, password=self.password)

        # Logout qilamiz
        response = self.client.get(reverse("users:logout"))

        # Redirect bo‘lishini tekshiramiz
        self.assertRedirects(response, reverse("landing"))
