from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role =='Admin'

@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'admin_view.html')