from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
from .models import Books, Book_category,Loan
from .forms import RegisterBook
# Create your views here.

#pagina de home

def home(request):
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user']) #id do user na session
        books = Books.objects.filter(user = user)
        form = RegisterBook()
        form.fields['user'].initial = request.session['user'] #fazendo o valor inicial ser pre-definido
        form.fields['book_category'].queryset =  Book_category.objects.filter(user = user)
        
        return render(request, 'home.html', {'books': books, 
                                             'user_authenticated': request.session.get('user'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')


#parar ver os livros 

def book_views(request, id): #passando a request + o id do livro solicitado
    if request.session.get('user'):
        books = Books.objects.get(id = id) #pega apenas o do botao acessar
        if request.session.get('user') == books.user.id:
            category_book = Book_category.objects.filter(user = request.session.get('user'))
            loans = Loan.objects.filter(book = books)
            return render(request, 'book_views.html', {'book': books, 
                                                       'category_book': category_book, 
                                                       'loans': loans,
                                                       'book_id': id})
        else:
            return HttpResponse('livro não encontrado')
    return redirect('/auth/login/?status=2')

# registrar um livro
def register_book(request):
    if request.method == 'POST':
        form = RegisterBook(request.POST)
        #se o formulario for valido
        if form.is_valid():
            form.save()
            return redirect('/book/home')
        else:
            return HttpResponse("Dados invalidos")

#registrar a categoria do livro
def register_category_book(request):
    if request.method == 'POST':
        category_name = request.POST['category_name']
        description = request.POST['description']
        user_id = request.session.get('user')
        
        if user_id:
            user = User.objects.get(id=user_id)
            category = Book_category(user=user, name=category_name, description = description)
            category.save()
            return redirect('/book/home')
        else:
            return HttpResponse('Usuário não autenticado')
    else:
        return HttpResponse('Método inválido')


# deletar um livro (Bug)
def delete_book(request,id):
    book = Books.objects.get(id = id).delete()
    return redirect('/book/home')