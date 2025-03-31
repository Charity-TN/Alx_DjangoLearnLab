from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

#Custom adnim display
    search_fields = ('title', 'author')

#Enable search by title and author
    list_filter = ('publication_year',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import MyModel

def setup_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(MyModel)

    permissions = [
        Permission.objects.get(codename="can_view", content_type=content_type),
        Permission.objects.get(codename="can_create", content_type=content_type),
        Permission.objects.get(codename="can_edit", content_type=content_type),
        Permission.objects.get(codename="can_delete", content_type=content_type),
    ]

    groups = {
        "Viewers": [permissions[0]],
        "Editors": [permissions[1], permissions[2]],
        "Admins": permissions,
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        group.permissions.set(perms)

# Call this function in a migration or Django shell to set up groups.