from django.contrib.auth import get_user_model
from django.db import transaction
from apps.users.models import User as UserType

User = get_user_model()

def user_create(*, username: str, email: str, password: str, **extra_fields) -> UserType:
    """
    Service to create a user.
    """
    user = User(username=username, email=email, **extra_fields)
    user.set_password(password)
    
    with transaction.atomic():
        user.save()
        
    return user

def user_update(*, user: UserType, data) -> UserType:
    """
    Service to update a user.
    """
    non_side_effect_fields = ['first_name', 'last_name', 'email']
    
    for field in non_side_effect_fields:
        if field in data:
            setattr(user, field, data[field])
            
    user.save()
    return user
