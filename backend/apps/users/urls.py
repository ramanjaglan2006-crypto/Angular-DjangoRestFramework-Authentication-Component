from django.urls import path
from .views import UserRetrieveUpdateView

app_name = 'users'

urlpatterns = [
    path('me/', UserRetrieveUpdateView.as_view(), name='user-me'),
]
