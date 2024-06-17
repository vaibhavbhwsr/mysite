import pytest
from mixer.backend.django import mixer
from django.utils import timezone
from post.models import Post  # Import your Post model
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def sample_user():
    return mixer.blend(User)


@pytest.fixture
def sample_post(sample_user):
    return mixer.blend(Post, user_name=sample_user)


@pytest.mark.django_db
class TestPostModel:

    def test_post_creation(self, sample_post):
        assert sample_post.pk is not None
        assert sample_post.user_name is not None
        assert sample_post.description == sample_post.description  # Check other fields similarly

    def test_post_created_at(self, sample_post):
        assert sample_post.created_at is not None
        assert sample_post.created_at <= timezone.now()

    def test_post_modified_at(self, sample_post):
        initial_modified_at = sample_post.modified_at
        sample_post.save()
        assert sample_post.modified_at >= initial_modified_at

    def test_soft_delete(self, sample_post):
        # Ensure the instance is not deleted initially
        assert sample_post.is_deleted is False

        # Perform soft delete
        sample_post.soft_delete()

        # Check that is_deleted is set to True
        assert sample_post.is_deleted is True

        # Ensure the instance is not in the NotDeleted manager's queryset
        assert sample_post not in Post.objects.all()

        # Ensure the instance is still in the all_object manager's queryset
        assert sample_post in Post.all_object.all()

    def test_restore(self, sample_post):
        # Soft delete the instance first
        sample_post.soft_delete()
        assert sample_post.is_deleted is True

        # Restore the instance
        sample_post.restore()

        # Check that is_deleted is set to False
        assert sample_post.is_deleted is False

        # Ensure the instance is in the NotDeleted manager's queryset
        assert sample_post in Post.objects.all()
