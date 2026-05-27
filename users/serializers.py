from rest_framework import serializers
from .models import User
from django.core.validators import EmailValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[EmailValidator(message="Invalid email format")],
        required=True
    )
    name = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'created_at']
        read_only_fields = ['id', 'created_at']
