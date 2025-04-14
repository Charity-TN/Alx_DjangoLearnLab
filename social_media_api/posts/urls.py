from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import FollowUserAPIView, UnfollowUserAPIView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserAPIView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
]

from django.urls import path
from .views import UserFeedAPIView

urlpatterns = [
    path('feed/', UserFeedAPIView.as_view(), name='user-feed'),
]

from django.urls import path
from .views import LikePostAPIView, UnlikePostAPIView

urlpatterns = [
    path('<int:pk>/like/', LikePostAPIView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='unlike-post'),
]