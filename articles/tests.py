from django.test import TestCase

from .models import Category,Article

# TestCase tells Django that this class contains tests.
# Django creates a temporary test database (not your real database).
# All tests run using the temporary database.
# When the tests finish, Django automatically destroys the test database.
class CategoryModelTests(TestCase):
    # this piece of code(method) Checks that when a new Category is created, the slug is automatically generated 
    # from the name.
    def test_save_generates_slug_from_name(self):
        category = Category.objects.create(name="Science Fiction")

        self.assertEqual(category.slug, "science-fiction")


# this test makes sure slug and name are compatible
class ArticleModelTests(TestCase):
    def test_save_generates_slug_from_name(self):
        article = Article.objects.create(name="The Great Gatsby")

        self.assertEqual(article.slug, "the-great-gatsby")
    # If the name is updated using update_fields, the slug should be updated too.
    def test_save_accepts_standard_django_arguments(self):
        article = Article.objects.create(name="Dune")

        article.name = "Dune Messiah"
        article.save(update_fields=["name"])
        article.refresh_from_db()

        self.assertEqual(article.name, "Dune Messiah")
        self.assertEqual(article.slug, "dune-messiah")




