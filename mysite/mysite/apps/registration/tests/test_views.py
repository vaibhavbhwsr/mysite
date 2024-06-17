import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()


@pytest.mark.django_db
class TestSignupView:

    def test_signup_view_renders_for_anonymous_user(self):
        client = Client()
        response = client.get(reverse('signup'))
        assert response.status_code == 200
        assert 'form' in response.context

    def test_signup_view_redirects_logged_in_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('signup'))
        assert response.status_code == 302
        assert response.url == reverse('home')

    def test_signup_view_creates_user(self):
        client = Client()
        response = client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
            'email': 'newuser@example.com'
        })
        assert response.status_code == 302
        assert response.url == '/'
        assert User.objects.filter(username='newuser').exists()
