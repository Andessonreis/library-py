from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
from .models import Books, Book_category,Loan
from .forms import RegisterBook
# Create your views here.

def home(request):
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        books = Books.objects.filter(user = user)
        form = RegisterBook()
        

        return render(request, 'home.html', {'books': books, 
                                             'user_authenticated': request.session.get('user'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')


def book_views(request, id): #passando a request + o id do livro solicitado
    if request.session.get('user'):
        books = Books.objects.get(id = id) #pega apenas o do botao acessar
        if request.session.get('user') == books.user.id:
            category_book = Book_category.objects.filter(user = request.session.get('user'))
            loans = Loan.objects.filter(book = books)
            return render(request, 'book_views.html', {'book': books, 'category_book': category_book, 'loans': loans})
        else:
            return HttpResponse('livro não encontrado')
    return redirect('/auth/login/?status=2')


def register_book(request):
    if request.method == 'POST':
        form = RegisterBook(request.POST)
        #se o formulario for valido
        if form.is_valid():
            form.save()
            return HttpResponse("salvo")
        else:
            return HttpResponse("Dados invalidos")



