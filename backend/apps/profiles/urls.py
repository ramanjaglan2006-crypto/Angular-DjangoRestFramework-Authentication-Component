from django.urls import path
from .views import ProfileRetrieveUpdateView

app_name = 'profiles'

urlpatterns = [
    path('me/', ProfileRetrieveUpdateView.as_view(), name='profile-me'),
]
