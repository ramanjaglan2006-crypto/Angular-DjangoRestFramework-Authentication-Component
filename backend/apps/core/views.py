from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root_view(request):
    """
    API overview showing available endpoints.
    """
    return Response({
        "authentication": {
            "register": "/api/v1/auth/register/",
            "login": "/api/v1/auth/login/",
            "token_refresh": "/api/v1/auth/token/refresh/",
            "password_reset": "/api/v1/auth/password-reset/",
        },
        "users": {
            "me": "/api/v1/users/me/",
        },
        "profiles": {
            "me": "/api/v1/profiles/me/",
        }
    })
