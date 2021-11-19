# This is a common file to set up testings and can be used in every project
from django.test import TestCase
from django.contrib.auth.models import User


class TestModel(TestCase):
    def setUp(self):
        print("\nTest Started!")
        self.user = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "asdf@123",
            "password2": "asdf@123",
        }

    def create_test_user(self):
        user = User.objects.create(username="test_user", email="test_user@example.com")
        user.set_password("asdf@123")
        user.save()
        return user

    def tearDown(self):
        print("Test Finished!")
        return super().tearDown()
