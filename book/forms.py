from django import forms
from .models import Books, Book_category


class RegisterBook(forms.ModelForm):
    class Meta: #usando para refenciar informaçoes do formulario
        model = Books
        fields = "__all__"

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs) ## usando super para pegar a funçao da class pai e rodar jnto/basemodelforms
        self.fields['user'].widget = forms.HiddenInput() #mudando a chave estrangeira q era select

class CategoryBook(forms.ModelForm):
    class Meta: #usando para refenciar informaçoes do formulario
        model = Book_category
        fields = "__all__"

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs) ## usando super para pegar a funçao da class pai e rodar jnto/basemodelforms
        self.fields['book_category'].widget = forms.HiddenInput() #mudando a chave estrangeira q era select