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

    def test_login_view_redirects_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('login'))
        assert response.status_code == 302
        assert response.url == '/'

    def test_login_view_shows_success_message(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        }, follow=True)
        assert response.status_code == 200

    def test_profile_view_requires_login(self):
        client = Client()
        response = client.get(reverse('profile'))
        assert response.status_code == 302
        assert response.url.startswith(reverse('login'))

    def test_profile_view_renders_for_logged_in_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('profile'))
        assert response.status_code == 200
        assert 'registration/profile.html' in [t.name for t in response.templates]

    def test_update_profile_view_requires_login(self):
        client = Client()
        response = client.get(reverse('update-profile'))
        assert response.status_code == 302
        assert response.url.startswith(reverse('login'))

    def test_update_profile_view_updates_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.post(reverse('update-profile'), {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        }, follow=True)
        assert response.status_code == 200
        user.refresh_from_db()
        assert user.username == 'updateduser'
        assert user.first_name == 'Updated'
        assert user.last_name == 'User'
        assert user.email == 'updated@example.com'
