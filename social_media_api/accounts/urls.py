from django.urls import path
from .views import RegistrationAPIView, CustomObtainAuthToken, UserProfileAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]

from django.urls import path
from .views import FollowUserAPIView, UnfollowUserAPIView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserAPIView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
]