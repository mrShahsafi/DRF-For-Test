from rest_framework import serializers
from .models import User


class TokenAuthenticationSerializer(serializers.ModelSerializer)
    password2 = serializers.CharField(
                            style={
                                    'input_type': 'password'
                                    }
                                    ,
                            write_only=True
                                            )
    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')
