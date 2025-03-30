This is a Django Project for managing a library system.

# Role-Based Access Control in Django
1. Custom permissions are defined in the `MyModel` class with the variables can_view, can_create, can_edit,can_delete.
2. Groups and permissions can be configured via the setup script in `admin.py`.
3. Permissions are enforced in views using Django's `permission_required` decorator.
4. Tested the implementation of the permissions and groups manually.