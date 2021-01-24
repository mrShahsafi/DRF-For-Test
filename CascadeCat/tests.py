from django.test import TestCase
from .models import Product, Category, SubCategory


class TestForCreateProduct(TestCase):
    def setUp(self):
        product = Product.objects.create(name='test product',
                                barcode='21314151',
                                )

    def test_animals_can_speak(self):
        """Product with 123456789 barcode"""
        try:
            test_get = Product.objects.get(barcode=123456789)
        except:
            print('file not found 4O4')
