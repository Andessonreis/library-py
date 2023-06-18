from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), #url estatica
    path('book_views/<int:id>', views.book_views, name='book_views') #url dinamica
]