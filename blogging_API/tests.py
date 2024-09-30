from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title="Test Post",
            content="This is a test content for the blog post.",
            category="Technology",
            tags="Tech"
        )

    def test_post_creation(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.category, "Technology")