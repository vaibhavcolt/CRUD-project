from .models import User
from rest_framework.exceptions import NotFound

class UserService:
    @staticmethod
    def create_user(validated_data):
        """
        Creates a new user. The validated_data is assumed to be clean
        and checked for uniqueness by the serializer.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            role=validated_data['role']
        )
        return user

    @staticmethod
    def get_all_users():
        """
        Returns a queryset of all users. Can be chained with filters/pagination in views.
        """
        return User.objects.all().order_by('-created_at')

    @staticmethod
    def get_user_by_id(user_id):
        """
        Fetches a user by ID or raises NotFound exception (handled by our custom handler).
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
