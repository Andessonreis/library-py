from django import forms
from .models import Books

class RegisterBook(forms.ModelForm):
    class Meta: #usando para refenciar informaçoes do formulario
        model = Books
        fields = ('name', 'author', 'co_author', 'register_date', 'borrowed', 'book_category')


