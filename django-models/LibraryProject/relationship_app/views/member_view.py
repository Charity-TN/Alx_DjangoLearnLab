from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def member_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role =='Member'

@user_passes_test(member_required)
def member_view(request):
    return render(request, 'member_view.html')