from django.test import TestCase
from .models import Product, Category, SubCategory


class TestForCreateProduct(TestCase):
    def setUp(self):
        product = Product.objects.create(name='test product',
                                barcode='21314151',
                                category__id=1
                                )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
