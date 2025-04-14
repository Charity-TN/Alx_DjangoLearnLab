from django.urls import path
from .views import RegistrationAPIView, CustomObtainAuthToken, UserProfileAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]