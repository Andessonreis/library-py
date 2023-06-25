from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
from .models import Books, Book_category, Loan
from .forms import RegisterBook
from django.contrib import messages

# Create your views here.

# pagina de home


def home(request):
    if request.session.get("user"):
        user = User.objects.get(id=request.session["user"])  # id do user na session
        books = Books.objects.filter(user=user)
        form = RegisterBook()
        form.fields["user"].initial = request.session[
            "user"
        ]  # fazendo o valor inicial ser pre-definido
        form.fields["book_category"].queryset = Book_category.objects.filter(user=user)
        users = User.objects.all()
        lend_books = Books.objects.filter(user = user).filter(borrowed = False)
        all_books = books.count()

        loaned_books = Books.objects.filter(user = user).filter(borrowed = True)

        return render( #enviando para o html
            request,
            "home.html",
            {
                "books": books,
                "user_authenticated": request.session.get("user"),
                "form": form,
                "users": users,
                "lend_books": lend_books,
                "all_books": all_books,
                "loaned_books":loaned_books,
            },
        )
    else:
        return redirect("/auth/login/?status=2")


# parar ver os livros
def book_views(request, id):  # passando a request + o id do livro solicitado
    if request.session.get("user"):
        books = Books.objects.get(id=id)  # pega apenas o do botao acessar
        if request.session.get("user") == books.user.id:
            category_book = Book_category.objects.filter(
                user=request.session.get("user")
            )
            loans = Loan.objects.filter(book=books)
            books_all = Books.objects.filter(user_id = request.session.get('user'))
            return render(
                request,
                "book_views.html",
                {
                    "book": books,
                    "category_book": category_book,
                    "loans": loans,
                    "book_id": id,
                    "books_all" : books_all
                },
            )
        else:
            return HttpResponse("livro não encontrado")
    return redirect("/auth/login/?status=2")


# registrar um livro
def register_book(request):
    if request.method == "POST":
        form = RegisterBook(request.POST)
        # se o formulario for valido
        if form.is_valid():
            form.save()
            return redirect("/book/home")
        else:
            return HttpResponse("Dados invalidos")


# registrar a categoria do livro
def register_category_book(request):
    if request.method == "POST":
        category_name = request.POST["category_name"]
        description = request.POST["description"]
        user_id = request.session.get("user")

        if user_id:
            user = User.objects.get(id=user_id)
            category = Book_category(
                user=user, name=category_name, description=description
            )
            category.save()
            messages.success(request, "Categoria de livro registrada com sucesso!")
            return redirect("/book/home/?status=5")
        else:
            return HttpResponse("Usuário não autenticado")
    else:
        return HttpResponse("Método inválido")


# deletar um livro (Bug)
def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect("/book/home")

#cadastrar emprestimo
def register_loan(request):
    if request.method == 'POST':
        name_borrowed_id = request.POST.get('name_borrowed')
        selected_book_id = request.POST.get('selected_book')

        name_borrowed = User.objects.get(id=name_borrowed_id)

        loan = Loan(name_borrowed=name_borrowed, book_id=selected_book_id)
        loan.save()

        book = Books.objects.get(id=selected_book_id)
        book.borrowed = True
        book.save()


        return redirect("/book/home")