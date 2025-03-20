from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

from .models import Library
from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(library=self.object)
        return context
    

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return redirect("home")
        else:
            form = UserCreationForm()
        return render(request,"relationship_app/register.html",{"form: form"})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate

def login_view(request):
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def register_view(request):
    return render(request, 'register.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def librarian_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def member_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
    
@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'adnim_view.html')    

@user_passes_test(librarian_required)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(member_required)
def member_view(request):
    return render(request, 'member_view.html')        