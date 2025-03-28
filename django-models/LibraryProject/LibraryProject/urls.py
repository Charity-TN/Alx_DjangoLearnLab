"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from relationship_app.views import register
from relationship_app import views
from django.urls import include
from relationship_app.views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(),name='library_detail'),
    path('login/',auth_views.LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'),name='logout'),
    path('register/',register,name='register'),
    path('relationship/', include('relationship_app.urls')),
    path('admin_page/', admin_view, name='admin_view'),
    path('librarian_page/', librarian_view, name='librarian_view'),
    path('member_page/', member_view, name='member_view'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.delete_book, name='delete_book'),
]
