from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class Testcaselogin(TestCase):
    def setUp(self):
        self.username = "TestUser123"
        self.password = "Admin111"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        
    def test_login_valid(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post(reverse("users:login"), data=data)

        self.assertRedirects(response, reverse("landing_page")) 
        user = User.objects.get(username=self.username)
        self.assertTrue(user.is_authenticated)