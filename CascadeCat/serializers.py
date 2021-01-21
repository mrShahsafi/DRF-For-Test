from rest_framework import serializers
from .models import Product
class SingleProductSerializer(serializers.ModelSerializer):
    #StringRelatedField returns __str__ func of ForeignKey
    category = serializers.StringRelatedField(
                                    many=True
                                    )
    sub_category = serializers.StringRelatedField(
                                    many=True
                                    )
    class Meta:
        model = Product
        fields = [
        'name',
        'barcode',
        'slug',
        'category',
        'sub_category'
        ]
