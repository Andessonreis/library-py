from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
from .models import Books
# Create your views here.

def home(request):
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        books = Books.objects.filter(user = user)
        return render(request, 'home.html', {'books': books})
    else:
        return redirect('/auth/login/?status=2')


def book_views(request, id): #passando a request + o id do livro solicitado
    books = Books.objects.get(id = id) #pega apenas o do botao acessar
    return render(request, 'book_views.html', {'book': books})