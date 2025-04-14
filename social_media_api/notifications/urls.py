from django.urls import path
from .views import UserNotificationsAPIView

urlpatterns = [
    path('', UserNotificationsAPIView.as_view(), name='notifications-list'),
]