from django.contrib.auth import get_user_model
from apps.users.models import User as UserType

User = get_user_model()

def user_get_by_id(user_id: int) -> UserType:
    """
    Selector to get a user by ID.
    """
    return User.objects.get(id=user_id)

def user_list() -> list[UserType]:
    """
    Selector to list all users.
    """
    return User.objects.all()
