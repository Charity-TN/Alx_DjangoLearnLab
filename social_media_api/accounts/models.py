

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following', 
        blank=True
    )

    def follow(self, user):
        """Follow a user"""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user"""
        self.following.remove(user)

    def is_following(self, user):
        """Check if following a user"""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username