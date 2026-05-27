from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve and update the authenticated user's profile.
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
