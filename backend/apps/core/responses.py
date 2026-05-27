from rest_framework.response import Response

class APIResponse(Response):
    """
    Standardized API response formatter.
    """
    def __init__(self, data=None, status=None, message="Success", **kwargs):
        formatted_data = {
            "status": "success" if status is None or status < 400 else "error",
            "message": message,
            "data": data,
        }
        super().__init__(data=formatted_data, status=status, **kwargs)
