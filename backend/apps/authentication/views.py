from rest_framework import generics, permissions
from apps.users.serializers import UserCreateSerializer
from apps.core.responses import APIResponse
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user.
    """
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return APIResponse(
            data=UserCreateSerializer(user).data,
            status=status.HTTP_201_CREATED,
            message="User registered successfully"
        )
