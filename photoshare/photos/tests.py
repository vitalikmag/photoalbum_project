from django.test import TestCase

from .models import Category, Photo


class MyModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.photo = Photo.objects.create(category=self.category, description='Test photo description')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_photo_str(self):
        self.assertEqual(str(self.photo), 'Test photo description')

    def test_photo_category(self):
        self.assertEqual(self.photo.category, self.category)
