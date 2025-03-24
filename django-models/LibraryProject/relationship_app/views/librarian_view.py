from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def librarian_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role =='Librarian'

@user_passes_test(librarian_required)
def librarian_view(request):
    return render(request, 'librarian_view.html')