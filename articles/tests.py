from django.test import TestCase

from .models import Category


class CategoryModelTests(TestCase):
    # this piece of code(method) Checks that when a new Category is created, the slug is automatically generated 
    # from the name.
    def test_save_generates_slug_from_name(self):
        category = Category.objects.create(name="Science Fiction")

        self.assertEqual(category.slug, "science-fiction")

    # Checks that overriding the save() method does not break Django's standard save() arguments.
    def test_save_accepts_standard_django_arguments(self):
        category = Category.objects.create(name="History")

        category.name = "World History"
        category.save(update_fields=["name"])
