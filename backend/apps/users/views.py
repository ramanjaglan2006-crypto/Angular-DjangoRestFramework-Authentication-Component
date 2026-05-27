from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve and update the authenticated user's details.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
