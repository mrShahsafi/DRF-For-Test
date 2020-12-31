from .models import Hero
from rest_framework import serializers


class SingleHeroSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,
                                 allow_null=False,
                                 allow_blank=False,
                                 max_length=60,
                                 )
    alias = serializers.CharField(required=True,
                                     allow_null=False,
                                     allow_blank=False,
                                     max_length=60,
                                     )
    world = serializers.CharField(required=True,
                                     allow_null=False,
                                     allow_blank=False,
                                     max_length=60,
                                     )

class SubmitHeroSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,
                                 allow_null=True,
                                 allow_blank=True,
                                 max_length=60,
                                 )
    alias = serializers.CharField(required=True,
                                     allow_null=True,
                                     allow_blank=True,
                                     max_length=60,
                                     )
    world_id = serializers.IntegerField(required=True,
                                     allow_null=True,
                                     )
