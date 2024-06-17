import pytest
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from mixer.backend.django import mixer
import io
from PIL import Image

from post.models import Post, Comment


@pytest.fixture
def user(db, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='12345')
    return user


@pytest.fixture
def authenticated_client(client, user):
    client.login(username='testuser', password='12345')
    return client


@pytest.fixture
def post(user):
    return mixer.blend(Post, user_name=user, date_posted=timezone.now())


def generate_image_file():
    file = io.BytesIO()
    image = Image.new('RGB', (100, 100))
    image.save(file, 'jpeg')
    file.name = 'test_image.jpg'
    file.seek(0)
    return SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')


def test_home_view(authenticated_client):
    response = authenticated_client.get(reverse('home'))
    assert response.status_code == 200
    assert 'post/home.html' in [t.name for t in response.templates]
    assert 'posts' in response.context


def test_post_create_view(authenticated_client):
    response = authenticated_client.get(reverse('create-post'))
    assert response.status_code == 200
    assert 'post/create_post.html' in [t.name for t in response.templates]

    image = generate_image_file()
    data = {
        'description': 'New post description',
        'tags': 'tag1, tag2',
        'picture': image
    }
    response = authenticated_client.post(reverse('create-post'), data, format='multipart')
    assert response.status_code == 302  # Redirects after successful post creation
    assert Post.objects.filter(description='New post description').exists()
    post = Post.objects.get(description='New post description')
    assert post.picture


def test_post_detail_view(authenticated_client, post):
    response = authenticated_client.get(reverse('detail', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert 'post/detail.html' in [t.name for t in response.templates]
    assert response.context['post'] == post


def test_like_view(authenticated_client, post):
    response = authenticated_client.post(reverse('like', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert post.likes.filter(id=authenticated_client.session['_auth_user_id']).exists()

    response = authenticated_client.post(reverse('like', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert not post.likes.filter(id=authenticated_client.session['_auth_user_id']).exists()


def test_post_delete_view(authenticated_client, post):
    response = authenticated_client.post(reverse('post-delete', kwargs={'pk': post.pk}))
    assert response.status_code == 302
    assert not Post.objects.filter(id=post.pk).exists()


def test_post_update_view(authenticated_client, post):
    response = authenticated_client.get(reverse('post-update', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert 'post/create_post.html' in [t.name for t in response.templates]

    image = generate_image_file()
    data = {
        'description': 'Updated description',
        'tags': 'updated tag',
        'picture': image
    }
    response = authenticated_client.post(reverse('post-update', kwargs={'pk': post.pk}), data, format='multipart')
    assert response.status_code == 302
    post.refresh_from_db()
    assert post.description == 'Updated description'
    assert post.picture


def test_post_comment_view(authenticated_client, post):
    data = {'comment_text': 'This is a comment'}
    response = authenticated_client.post(reverse('create-comment', kwargs={'pk': post.pk}), data)
    assert response.status_code == 200
    assert Comment.objects.filter(comment_text='This is a comment').exists()
    comment = Comment.objects.get(comment_text='This is a comment')
    assert comment.user.username == 'testuser'
    assert comment.post == post
