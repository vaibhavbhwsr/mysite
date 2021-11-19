from mysite.commons.setup_test import TestModel
from django.contrib.auth.models import User


class TestModelUser(TestModel):
    def test_should_create_user(self):
        # Created user 'test_user' for test
        user = self.create_test_user()

        self.assertEqual(str(user), user.username)
