from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Custom exception handler to provide a consistent response format.
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            'status': 'error',
            'message': response.data.get('detail', 'An error occurred'),
            'errors': response.data if isinstance(response.data, dict) and 'detail' not in response.data else None
        }
    else:
        # For unhandled exceptions
        return Response({
            'status': 'error',
            'message': str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
