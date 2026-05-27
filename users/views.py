from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer
from .services import UserService
from .utils import success_response

class UserListCreateAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    # Apply filters and search backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'email']
    
    def get_permissions(self):
        # Allow any for POST (registration), but require auth for GET (list)
        # Assuming JWT is a bonus, let's make it AllowAny for now so it's easy to test without tokens, 
        # but if we want strict JWT, we can change it to IsAuthenticated.
        return [AllowAny()]

    def get_queryset(self):
        # Fetch from service layer
        return UserService.get_all_users()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        # Pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            # Custom formatting for paginated response
            data = {
                "count": paginated_response.data['count'],
                "next": paginated_response.data['next'],
                "previous": paginated_response.data['previous'],
                "results": serializer.data
            }
            return success_response("Users fetched successfully", data)

        serializer = self.get_serializer(queryset, many=True)
        return success_response("Users fetched successfully", serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Use service to create
        user = UserService.create_user(serializer.validated_data)
        
        response_serializer = self.get_serializer(user)
        return success_response("User created successfully", response_serializer.data, status_code=201)

class UserDetailAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Keeping it open for easy testing of assignment

    def get(self, request, pk, *args, **kwargs):
        # Fetch from service layer, this raises NotFound if user doesn't exist
        user = UserService.get_user_by_id(pk)
        
        serializer = self.get_serializer(user)
        return success_response("User fetched successfully", serializer.data)
