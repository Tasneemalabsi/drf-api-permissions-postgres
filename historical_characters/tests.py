from django.test import TestCase
from django.contrib.auth.models import User

from .models import Character


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a blog post
        test_character = Character.objects.create(
            writer=testuser1, name="Blog title", description="Body content..."
        )
        test_character.save()

    def test_blog_content(self):
        character = Character.objects.get(id=1)
        expected_author = f"{character.writer}"
        expected_title = f"{character.name}"
        expected_body = f"{character.description}"
        self.assertEqual(expected_author, "testuser1")
        self.assertEqual(expected_title, "Blog title")
        self.assertEqual(expected_body, "Body content...")