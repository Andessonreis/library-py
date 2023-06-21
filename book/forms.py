from django import forms
from .models import Books


class RegisterBook(forms.ModelForm):
    class Meta: #usando para refenciar informaçoes do formulario
        model = Books
        fields = "__all__"

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs) ## usando super para pegar a funçao da class pai e rodar jnto/basemodelforms
