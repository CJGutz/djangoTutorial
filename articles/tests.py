from django.test import TestCase
from django.contrib.auth.models import User

from articles.models import Article

class ArticleModelTest(TestCase):
    """Tests model logic in article"""

    def test_article_snippet_length(self):
        """Tests that a snippet is never more than 53 chars"""

        hundred_char_string = "a" * 100
        fifty_char_string = "b" * 50
        ten_char_string = "c" * 10

        user = User.objects.create()

        article1 = Article.objects.create(title="Article 1", body=hundred_char_string, author=user)
        article2 = Article.objects.create(title="Article 2", body=fifty_char_string, author=user)
        article3 = Article.objects.create(title="Article 3", body=ten_char_string, author=user)

        self.assertEqual(len(article1.snippet()), 53)
        self.assertEqual(len(article2.snippet()), 50)
        self.assertEqual(len(article3.snippet()), 10)
