from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponseForbidden

@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    # Add your edit logic here
    return render(request, 'edit.html')

@permission_required('app_name.can_view', raise_exception=True)
def view_view(request):
    # Add your view logic here
    return render(request, 'view.html')