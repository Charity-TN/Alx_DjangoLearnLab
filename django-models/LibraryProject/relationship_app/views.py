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
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def check_role(user,required_role):
    try:
        return user.userprofile.role == required_role
    except UserProfile.DoesNotExist:
        return False
    
def admin_check(user):
    return check_role(user, 'Admin')

def librarian_check(user):
    return check_role(user, 'Librarian')

def member_check(user):
    return check_role(user, 'Member')

@login_required
@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html', {'user': request.user})

@login_required
@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html', {'user': request.user})

@login_required
@user_passes_test(admin_check)
def member_view(request):
    return render(request, 'member_view.html', {'user': request.user})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('book_list')
        return render(request, 'add_book.html')
    
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book= get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()

        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book= get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
    


    