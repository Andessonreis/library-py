from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), #url estatica
    path('book_views/<int:id>', views.book_views, name='book_views'), #url dinamica
    path('register_book', views.register_book, name='register_book'),
    path('register_category_book', views.register_category_book, name='register_category_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('register_loan', views.register_loan, name='register_loan'),
    path('return_books', views.return_books, name='return_books')
]